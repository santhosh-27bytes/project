const questions = [

"Explain the difference between Machine Learning and Deep Learning.",

"What is Overfitting in Machine Learning?",

"Explain the role of SQL in Data Analysis.",

"What is a Neural Network?",

"Describe a project you worked on."

];

let currentQuestion = 0;
let score = 0;

const questionElement =
document.getElementById("question");

const feedbackElement =
document.getElementById("feedback");

const scoreElement =
document.getElementById("score");

document
.getElementById("submitBtn")
.addEventListener("click", () => {

    const answer =
    document.getElementById("answer").value;

    if(answer.trim() === "")
    {
        alert("Please enter an answer.");
        return;
    }

    score += 20;

    feedbackElement.innerHTML =
    "Good attempt! AI evaluation will be connected from backend.";

    scoreElement.innerHTML =
    score + " / 100";
});

document
.getElementById("nextBtn")
.addEventListener("click", () => {

    currentQuestion++;

    if(currentQuestion >= questions.length)
    {
        alert("Interview Completed!");
        return;
    }

    questionElement.innerHTML =
    questions[currentQuestion];

    document.getElementById("answer").value = "";
});