document
.getElementById("loginForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    let email =
    document.getElementById("email").value;

    let password =
    document.getElementById("password").value;

    if(email === "" || password === "")
    {
        alert("Please fill all fields");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if(!response.ok)
        {
            alert(data.error || "Login failed");
            return;
        }

        alert(data.message || "Login Successful");

        window.location.href =
        "dashboard.html";
    }
    catch(error)
    {
        console.log(error);
        alert("Could not reach the server. Is the backend running?");
    }
});
