document
.getElementById("registerForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    let fullname =
    document.getElementById("fullname").value;

    let email =
    document.getElementById("email").value;

    let college =
    document.getElementById("college").value;

    let department =
    document.getElementById("department").value;

    let password =
    document.getElementById("password").value;

    let confirmPassword =
    document.getElementById("confirmPassword").value;

    if(password !== confirmPassword)
    {
        alert("Passwords do not match");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                fullname,
                email,
                college,
                department,
                password
            })
        });

        const data = await response.json();

        if(!response.ok)
        {
            alert(data.error || "Registration failed");
            return;
        }

        alert(data.message || "Registration Successful");

        window.location.href =
        "login.html";
    }
    catch(error)
    {
        console.log(error);
        alert("Could not reach the server. Is the backend running?");
    }
});
