const strategyBtn = document.getElementById("strategyBtn");

strategyBtn.addEventListener("click", async () => {

    const track = document.getElementById("track").value;
    const lap = document.getElementById("lap").value;
    const tire = document.getElementById("tire").value;
    const wear = document.getElementById("wear").value;
    const weather = document.getElementById("weather").value;
    const fuel = document.getElementById("fuel").value;

    const responseBox = document.getElementById("responseBox");

    responseBox.innerHTML = "Analyzing race telemetry...";

    const response = await fetch("/strategy", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            track,
            lap,
            tire,
            wear,
            weather,
            fuel
        })
    });

    const data = await response.json();

    responseBox.innerHTML = `
        <pre>${data.response}</pre>
    `;
});