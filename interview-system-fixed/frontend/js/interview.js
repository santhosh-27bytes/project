const questions = [

"Explain the difference between Machine Learning and Deep Learning.",

"What is Overfitting in Machine Learning?",

"Explain the role of SQL in Data Analysis.",

"What is a Neural Network?",

"Describe a project you worked on."

];

let currentQuestion = 0;
let totalScore = 0;
let answeredCount = 0;

const questionElement =
document.getElementById("question");

const questionNumberElement =
document.getElementById("questionNumber");

const feedbackElement =
document.getElementById("feedback");

const scoreElement =
document.getElementById("score");

document
.getElementById("submitBtn")
.addEventListener("click", async () => {

    const answerField = document.getElementById("answer");
    const answer = answerField.value;

    if(answer.trim() === "")
    {
        alert("Please enter an answer.");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/evaluate-answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ answer })
        });

        const data = await response.json();

        feedbackElement.innerHTML = data.feedback;

        answeredCount++;
        totalScore += data.score;

        const averageScore = Math.round(totalScore / answeredCount);
        scoreElement.innerHTML = averageScore + " / 100";
    }
    catch(error)
    {
        console.log(error);
        feedbackElement.innerHTML =
        "Could not reach the server. Is the backend running?";
    }
});

document
.getElementById("nextBtn")
.addEventListener("click", () => {

    currentQuestion++;

    if(currentQuestion >= questions.length)
    {
        alert("Interview Completed!");
        currentQuestion = questions.length - 1;
        return;
    }

    questionNumberElement.innerHTML =
    "Question " + (currentQuestion + 1);

    questionElement.innerHTML =
    questions[currentQuestion];

    document.getElementById("answer").value = "";
});
