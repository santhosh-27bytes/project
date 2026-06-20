console.log("Skill Gap Analysis Loaded");

const missingSkillsList = document.getElementById("missingSkillsList");

function renderMissingSkills(missingSkills) {
    if (!missingSkillsList) return;

    missingSkillsList.innerHTML = "";

    missingSkills.forEach(skill => {
        const li = document.createElement("li");
        li.textContent = `✗ ${skill}`;
        missingSkillsList.appendChild(li);
    });
}

fetch("http://localhost:5000/skill-gap?skills=Python,SQL,Machine%20Learning,HTML&career=AI%20Engineer")
.then(response => response.json())
.then(data => {
    console.log(data);
    renderMissingSkills(data.missing_skills);
})
.catch(error => {
    console.log("Could not load skill gap data, showing defaults.", error);
});
