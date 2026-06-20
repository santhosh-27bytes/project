console.log("Career Match Page Loaded");

const careerGrid = document.getElementById("careerGrid");

function matchLabel(score) {
    if (score >= 90) return "Best Match";
    if (score >= 75) return "Strong Match";
    if (score >= 50) return "Good Match";
    return "Potential Match";
}

function renderCareers(data) {
    if (!careerGrid) return;

    careerGrid.innerHTML = "";

    Object.entries(data).forEach(([career, score]) => {
        const card = document.createElement("div");
        card.className = "career-card";
        card.innerHTML = `
            <h2>${career}</h2>
            <div class="progress-bar">
                <div class="progress">${score}%</div>
            </div>
            <p>${matchLabel(score)}</p>
        `;
        careerGrid.appendChild(card);
    });
}

fetch("http://localhost:5000/career-match")
.then(response => response.json())
.then(data => {
    console.log(data);
    renderCareers(data);
})
.catch(error => {
    console.log("Could not load career match data, showing defaults.", error);
});
