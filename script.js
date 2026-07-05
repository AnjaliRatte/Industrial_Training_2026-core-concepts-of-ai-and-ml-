document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("click", () => {

        const page = card.dataset.page;

        const routes = {
            day1: "./pages/day1.html",
            day2: "./pages/day2.html",
            day3: "./pages/day3.html",
            projects: "./pages/projects.html",
            report: "./pages/report.html",
            certificates: "./pages/certificates.html"
        };

        if (routes[page]) {
            window.location.href = routes[page];
        } else {
            alert("Page not created yet 🚧");
        }

    });

});