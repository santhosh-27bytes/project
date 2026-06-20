from flask import Blueprint, jsonify, request
from services.career_recommender import recommend_career

career_bp = Blueprint(
    "career",
    __name__
)

@career_bp.route("/career-match", methods=["GET", "POST"])
def career_match():

    if request.method == "POST" and request.is_json:
        skills = request.json.get("skills", [])
    else:
        skills_param = request.args.get("skills", "")
        skills = [s.strip() for s in skills_param.split(",") if s.strip()]

    if not skills:
        skills = ["Python", "Machine Learning", "SQL"]

    results = recommend_career(skills)

    return jsonify(results)
