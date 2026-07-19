document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("click", () => {

        const page = card.dataset.page;

        const routes = {
            day1: "./pages/day1.html",
            day2: "./pages/day2.html",
            day3: "./pages/day3.html",
            day4: "./pages/day4.html",
            day5: "./pages/day5.html",
            day6: "./pages/day6.html",
            day7: "./pages/day7.html",
            day8: "./pages/day8.html",
            day9: "./pages/day9.html",
            day10: "./pages/day10.html",
            day11: "./pages/day11.html",
            day12: "./pages/day12.html",
            day13: "./pages/day13.html",
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