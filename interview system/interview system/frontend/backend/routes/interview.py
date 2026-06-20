from flask import Blueprint
from flask import request
from flask import jsonify
from services.interview_evaluator import evaluate_answer


interview_bp = Blueprint(
    "interview",
    __name__
)

@interview_bp.route(
    "/evaluate-answer",
    methods=["POST"]
)
def evaluate():

    answer =request.json["answer"]

    score = min(
        len(answer)//5,
        100
    )

    return jsonify({
        "score": score,
        "feedback":
        "Good attempt."
    })