console.log("Final Report Loaded");

document
.getElementById("downloadBtn")
.addEventListener("click", async () => {

    try {

        const response = await fetch(
            "http://localhost:5000/report/download"
        );

        if (!response.ok) {
            alert("Could not generate the report.");
            return;
        }

        const blob = await response.blob();

        const url =
        window.URL.createObjectURL(blob);

        const a =
        document.createElement("a");

        a.href = url;
        a.download = "CareerPilot_Report.pdf";

        a.click();

    }
    catch(error)
    {
        console.log(error);
        alert("Could not reach the server. Is the backend running?");
    }

});
