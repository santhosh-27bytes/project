document
.getElementById("analyzeBtn")
.addEventListener("click", () => {

    const file =
    document.getElementById("resumeFile").files[0];

    if(!file)
    {
        alert("Please upload a resume");
        return;
    }

    alert("Resume Uploaded Successfully");

    // Future API Call

    /*
    fetch("http://localhost:8000/analyze-resume",{
        method:"POST",
        body:formData
    })
    */

});