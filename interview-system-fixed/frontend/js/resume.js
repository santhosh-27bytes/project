document
.getElementById("analyzeBtn")
.addEventListener("click", async () => {

    const file =
    document.getElementById("resumeFile").files[0];

    if(!file)
    {
        alert("Please upload a resume");
        return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
        const response = await fetch("http://localhost:5000/upload-resume", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if(!response.ok)
        {
            alert(data.error || "Could not analyze resume");
            return;
        }

        alert("Resume Uploaded Successfully");

        const skillsList = document.getElementById("skillsList");
        if (skillsList && data.skills) {
            skillsList.innerHTML = "";
            data.skills.forEach(skill => {
                const li = document.createElement("li");
                li.textContent = skill;
                skillsList.appendChild(li);
            });
        }
    }
    catch(error)
    {
        console.log(error);
        alert("Could not reach the server. Is the backend running?");
    }

});
