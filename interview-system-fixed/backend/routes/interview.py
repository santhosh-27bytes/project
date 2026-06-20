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

    data = request.json or {}
    answer = data.get("answer", "")

    result = evaluate_answer(answer)

    return jsonify(result)
