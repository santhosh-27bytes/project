from flask import Blueprint, jsonify
from services.career_recommender import recommend_career

career_bp = Blueprint(
    "career",
    __name__
)

@career_bp.route("/career-match")
def career_match():

    return jsonify({

        "AI Engineer": 92,
        "Data Analyst": 85,
        "Software Engineer": 80,
        "Cyber Security": 72

    })