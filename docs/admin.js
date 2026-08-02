(function () {
  "use strict";

  /* Placeholder credentials only. Change these before treating login as secure. */
  var PLACEHOLDER_USER = "julie";
  var PLACEHOLDER_PASSWORD = "changeme2026";
  var AUTH_KEY = "julie_admin_preview_auth";
  var TRACKED_PAGES = [
    ["Home", "/"],
    ["Biography", "/bio.html"],
    ["Résumé", "/resume.html"],
    ["Violin / Viola résumé", "/resume1.html"],
    ["Educator résumé", "/resume2.html"],
    ["Jules Entertainment", "/jules.html"],
    ["Weddings", "/weddings.html"],
    ["Concerts in the Home", "/concerts.html"],
    ["Contact", "/contactus2.html"]
  ];

  var loginView = document.getElementById("adminLogin");
  var dashboardView = document.getElementById("adminDashboard");
  var form = document.getElementById("adminLoginForm");
  var message = document.getElementById("adminMessage");
  var logout = document.getElementById("adminLogout");

  function signedIn() {
    return sessionStorage.getItem(AUTH_KEY) === "yes";
  }

  function showDashboard() {
    loginView.hidden = true;
    dashboardView.hidden = false;
    loadAnalytics();
  }

  function showLogin() {
    dashboardView.hidden = true;
    loginView.hidden = false;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var user = document.getElementById("adminUsername").value.trim();
    var password = document.getElementById("adminPassword").value;

    if (user === PLACEHOLDER_USER && password === PLACEHOLDER_PASSWORD) {
      sessionStorage.setItem(AUTH_KEY, "yes");
      message.textContent = "";
      form.reset();
      showDashboard();
    } else {
      message.textContent = "That username or password does not match.";
    }
  });

  logout.addEventListener("click", function () {
    sessionStorage.removeItem(AUTH_KEY);
    showLogin();
  });

  function counterUrl(code, path) {
    return "https://" + code + ".goatcounter.com/counter/" + encodeURIComponent(path) + ".json";
  }

  async function fetchCount(code, path) {
    var response = await fetch(counterUrl(code, path), { cache: "no-store" });
    if (response.status === 404) return 0;
    if (!response.ok) throw new Error("Analytics returned " + response.status);
    var data = await response.json();
    return Number(String(data.count || "0").replace(/,/g, "")) || 0;
  }

  function formatNumber(value) {
    return new Intl.NumberFormat("en-US").format(value);
  }

  function renderRows(rows) {
    var body = document.getElementById("adminPageRows");
    body.innerHTML = rows
      .sort(function (a, b) { return b.count - a.count; })
      .map(function (row) {
        return "<tr><td>" + row.label + "</td><td>" + formatNumber(row.count) + "</td></tr>";
      })
      .join("");
  }

  function showSetupState() {
    document.getElementById("adminStatus").classList.remove("live");
    document.getElementById("adminStatusText").innerHTML =
      "The dashboard is ready, but real visitor tracking has not been connected yet. Add the GoatCounter site code in <code>analytics-config.js</code> to begin collecting visits.";
    document.getElementById("adminTotal").textContent = "—";
    document.getElementById("adminHome").textContent = "—";
    document.getElementById("adminTop").textContent = "—";
    document.getElementById("adminPageRows").innerHTML =
      '<tr><td colspan="2" class="admin-empty">No analytics data yet. Tracking starts after the analytics site code is connected.</td></tr>';
  }

  async function loadAnalytics() {
    var code = String((window.JULIE_ANALYTICS || {}).goatcounterCode || "").trim();
    if (!code) {
      showSetupState();
      return;
    }

    var status = document.getElementById("adminStatus");
    var statusText = document.getElementById("adminStatusText");
    status.classList.add("live");
    statusText.textContent = "Visitor tracking is connected and reporting live totals.";

    try {
      var results = await Promise.all(TRACKED_PAGES.map(async function (page) {
        return { label: page[0], path: page[1], count: await fetchCount(code, page[1]) };
      }));
      var total = await fetchCount(code, "TOTAL");
      var home = results.find(function (row) { return row.path === "/"; });
      var top = results.slice().sort(function (a, b) { return b.count - a.count; })[0];

      document.getElementById("adminTotal").textContent = formatNumber(total);
      document.getElementById("adminHome").textContent = formatNumber(home ? home.count : 0);
      document.getElementById("adminTop").textContent = top && top.count ? top.label : "—";
      renderRows(results);
    } catch (error) {
      status.classList.remove("live");
      statusText.textContent = "Analytics is configured, but totals could not be loaded. Confirm public visitor counters are enabled in GoatCounter.";
      document.getElementById("adminPageRows").innerHTML =
        '<tr><td colspan="2" class="admin-empty">Visitor totals are temporarily unavailable.</td></tr>';
    }
  }

  if (signedIn()) showDashboard();
  else showLogin();
})();
