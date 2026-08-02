(function () {
  "use strict";

  function addAdminLink() {
    var footer = document.getElementById("footer");
    if (!footer || footer.querySelector(".jm-admin-link")) return;

    var link = document.createElement("a");
    link.className = "jm-admin-link";
    link.href = "admin.html";
    link.textContent = "Admin login";
    link.setAttribute("aria-label", "Open the administrator login");
    footer.appendChild(link);
  }

  function enableAnalytics() {
    var config = window.JULIE_ANALYTICS || {};
    var code = String(config.goatcounterCode || "").trim();
    if (!code || location.protocol === "file:") return;

    var script = document.createElement("script");
    script.async = true;
    script.src = "https://gc.zgo.at/count.js";
    script.dataset.goatcounter = "https://" + code + ".goatcounter.com/count";
    document.head.appendChild(script);
  }

  function init() {
    addAdminLink();
    enableAnalytics();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
