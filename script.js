document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("click", () => {

    const page = card.dataset.page;

    console.log("Clicked page:", page);

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
            day13: "./pages/day13.html",
            day14: "./pages/day14.html",
            day15: "./pages/day15.html",
            day16: "./pages/day16.html",
            day17: "./pages/day17.html",
            day18: "./pages/day18.html",
            day19: "./pages/day19.html",
            day20: "./pages/day20.html",
            projects: "./pages/projects.html",
            report: "./pages/report.html",
            certificates: "./pages/certificates.html"
        };

            window.location.href = routes[page];
       

    });

});
