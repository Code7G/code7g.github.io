// Code7G site script: theme toggle and footer year. Loaded with "defer" on every page.
// The saved theme itself is applied by a tiny inline script in each page's <head>, before paint.
(function () {
    var root = document.documentElement;

    var year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();

    var toggle = document.getElementById("themeToggle");
    if (!toggle) return;

    function currentTheme() {
        var forced = root.getAttribute("data-theme");
        if (forced) return forced;
        return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }

    toggle.addEventListener("click", function () {
        var next = currentTheme() === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("c7g-theme", next); } catch (e) { /* storage blocked: theme still applies for this visit */ }
    });
})();
