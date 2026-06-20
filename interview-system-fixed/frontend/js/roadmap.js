console.log("Roadmap Page Loaded");

const roadmapContainer = document.getElementById("roadmapContainer");

function renderRoadmap(data) {
    if (!roadmapContainer) return;

    roadmapContainer.innerHTML = "";

    Object.entries(data).forEach(([month, topics]) => {
        const card = document.createElement("div");
        card.className = "month-card";

        const items = topics
            .map(topic => `<li>✓ ${topic}</li>`)
            .join("");

        card.innerHTML = `<h2>${month}</h2><ul>${items}</ul>`;
        roadmapContainer.appendChild(card);
    });
}

fetch("http://localhost:5000/roadmap?career=AI%20Engineer")
.then(response => response.json())
.then(data => {
    console.log(data);
    renderRoadmap(data);
})
.catch(error => {
    console.log("Could not load roadmap data, showing defaults.", error);
});
