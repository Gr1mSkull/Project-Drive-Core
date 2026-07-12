const API_BASE = "/api/v1";
const WS_URL = `${location.protocol === "https:" ? "wss" : "ws"}://${location.host}/ws/telemetry`;

const app = document.getElementById("app");
const statusBar = document.getElementById("status-bar");

let token = sessionStorage.getItem("dc_token") || "";
let telemetry = null;
let ws = null;

function route() {
  const hash = location.hash.replace(/^#/, "") || "/";
  document.querySelectorAll("nav a").forEach((a) => {
    a.classList.toggle("active", a.dataset.route === hash);
  });
  if (hash === "/service") return renderService();
  if (hash === "/logger") return renderLogger();
  return renderRace();
}

async function api(path, options = {}) {
  const headers = { ...(options.headers || {}) };
  if (token) headers.Authorization = `Bearer ${token}`;
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if (!res.ok) throw new Error(`${res.status} ${path}`);
  return res.json();
}

function connectWs() {
  if (ws) ws.close();
  ws = new WebSocket(WS_URL);
  ws.onopen = () => { statusBar.textContent = "Live"; };
  ws.onclose = () => {
    statusBar.textContent = "Disconnected — REST fallback";
    pollTelemetry();
  };
  ws.onmessage = (ev) => {
    try {
      const msg = JSON.parse(ev.data);
      if (msg.type === "telemetry") telemetry = msg;
    } catch (_) { /* ignore */ }
    route();
  };
}

async function pollTelemetry() {
  try {
    telemetry = await api("/telemetry");
    statusBar.textContent = "REST snapshot";
    route();
  } catch (_) {
    statusBar.textContent = "Offline (demo data)";
    telemetry = demoTelemetry();
    route();
  }
}

function demoTelemetry() {
  return {
    mode: "ENGINE_RUN",
    battery_v: 13.6,
    ecu: { rpm: 3200, coolant_c: 88, oil_kpa: 240, running: true },
    outputs: {
      fuel_pump: { state: "ON", a: 9.1, fault: null },
      fan1: { state: "ON", a: 21.3, fault: null },
      ecu_power: { state: "ON", a: 4.2, fault: null },
    },
    warnings: [],
  };
}

function renderRace() {
  const t = telemetry || demoTelemetry();
  const rpm = t.ecu?.rpm ?? "—";
  const clt = t.ecu?.coolant_c ?? "—";
  const oil = t.ecu?.oil_kpa ?? "—";
  const warns = (t.warnings || []).map((w) => `<div class="warn-banner">${w}</div>`).join("");
  const rows = Object.entries(t.outputs || {})
    .map(([name, o]) => `<tr><td>${name}</td><td class="state-${(o.state || "").toLowerCase()}">${o.state}</td><td>${o.a ?? "—"}A</td></tr>`)
    .join("");

  app.innerHTML = `
    <div class="race-grid">
      ${warns}
      <div>
        <div class="muted">RPM</div>
        <div class="rpm">${rpm}</div>
      </div>
      <div class="metrics">
        <div class="metric"><label>Mode</label>${t.mode || t.vehicle_mode || "—"}</div>
        <div class="metric"><label>Battery</label>${t.battery_v ?? "—"} V</div>
        <div class="metric"><label>CLT</label>${clt} °C</div>
        <div class="metric"><label>Oil</label>${oil} kPa</div>
      </div>
      <table><thead><tr><th>Output</th><th>State</th><th>Current</th></tr></thead><tbody>${rows}</tbody></table>
    </div>`;
}

async function renderService() {
  if (!token) {
    app.innerHTML = `
      <form class="pin-form" id="pin-form">
        <label>Service PIN</label>
        <input type="password" maxlength="6" pattern="[0-9]{6}" required />
        <button type="submit">Login</button>
      </form>`;
    document.getElementById("pin-form").onsubmit = async (e) => {
      e.preventDefault();
      const pin = e.target.querySelector("input").value;
      const res = await api("/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin }),
      });
      token = res.token;
      sessionStorage.setItem("dc_token", token);
      renderService();
    };
    return;
  }

  try {
    const outputs = await api("/outputs");
    const rows = (outputs.items || outputs).map((o) => `
      <tr>
        <td>${o.id}</td><td>${o.name}</td>
        <td class="state-${(o.state || "").toLowerCase()}">${o.state}</td>
        <td>${o.current_a ?? "—"}</td>
        <td>${o.fault ? `<span class="fault">${o.fault}</span>` : "—"}</td>
      </tr>`).join("");
    app.innerHTML = `<table>
      <thead><tr><th>Ch</th><th>Name</th><th>State</th><th>A</th><th>Fault</th></tr></thead>
      <tbody>${rows}</tbody></table>`;
  } catch (_) {
    const t = demoTelemetry();
    renderRace();
    app.insertAdjacentHTML("afterbegin", `<p class="warn-banner">Service API unavailable — demo data</p>`);
  }
}

function renderLogger() {
  app.innerHTML = `<p class="muted">Event log loads from GET /api/v1/events when ESP32 service is running.</p>`;
}

window.addEventListener("hashchange", route);
connectWs();
setInterval(() => { if (!ws || ws.readyState !== WebSocket.OPEN) pollTelemetry(); }, 3000);
route();
