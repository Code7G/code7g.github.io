// Code7G site script: theme toggle, footer year and scroll reveal. Loaded with "defer" on every page.
// The saved theme itself is applied by a tiny inline script in each page's <head>, before paint.
(function () {
    var root = document.documentElement;

    var year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();

    // Scroll reveal: cards and boxes fade and slide in the first time they scroll into view.
    // Skipped when the visitor asks for reduced motion or the browser has no IntersectionObserver,
    // so content is never left hidden.
    var calm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!calm && "IntersectionObserver" in window) {
        var items = document.querySelectorAll(".card, .point, .feature, .facts > div, .feature-graphic, .policy-list li, .contact-box");
        var seen = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                var el = entry.target;
                seen.unobserve(el);
                el.classList.add("is-visible");
                // Drop the reveal classes once the fade is done, so the card's own hover transition applies again.
                el.addEventListener("transitionend", function done(e) {
                    if (e.target !== el || e.propertyName !== "opacity") return;
                    el.removeEventListener("transitionend", done);
                    el.classList.remove("reveal", "is-visible");
                    el.style.removeProperty("--reveal-delay");
                });
            });
        }, { rootMargin: "0px 0px -8% 0px" });
        Array.prototype.forEach.call(items, function (el) {
            // Small stagger between siblings in the same grid, capped so long lists don't lag.
            var index = Array.prototype.indexOf.call(el.parentNode.children, el);
            el.style.setProperty("--reveal-delay", Math.min(index, 5) * 70 + "ms");
            el.classList.add("reveal");
            seen.observe(el);
        });
    }

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
