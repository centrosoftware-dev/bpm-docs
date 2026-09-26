(function () {
  function initials(name) {
    var parts = name.trim().split(/\s+/).filter(Boolean);
    if (parts.length === 0) return "";
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[1][0]).toUpperCase();
  }

  function escapeHtml(value) {
    var div = document.createElement("div");
    div.textContent = value;
    return div.innerHTML;
  }

  function render(host, displayName) {
    var wrap = document.createElement("div");
    wrap.className = "bpm-session";
    wrap.innerHTML =
      '<button type="button" class="bpm-session__toggle" aria-haspopup="true" aria-expanded="false">' +
        '<span class="bpm-session__avatar">' + escapeHtml(initials(displayName)) + '</span>' +
        '<span class="bpm-session__name">' + escapeHtml(displayName) + '</span>' +
        '<span class="bpm-session__chevron" aria-hidden="true">&#9662;</span>' +
      '</button>' +
      '<div class="bpm-session__menu">' +
        '<a href="/logout">Esci</a>' +
      '</div>';

    host.appendChild(wrap);

    var toggle = wrap.querySelector(".bpm-session__toggle");
    toggle.addEventListener("click", function (event) {
      event.stopPropagation();
      var open = wrap.classList.toggle("bpm-session--open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function () {
      wrap.classList.remove("bpm-session--open");
      toggle.setAttribute("aria-expanded", "false");
    });
  }

  function init() {
    var host = document.querySelector(".md-header__inner") || document.querySelector(".md-header");
    if (!host) return;

    fetch("/api/whoami", { credentials: "same-origin" })
      .then(function (res) { return res.ok ? res.json() : null; })
      .then(function (data) {
        if (data && data.displayName) render(host, data.displayName);
      })
      .catch(function () {});
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
