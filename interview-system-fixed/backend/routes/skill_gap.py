from flask import Blueprint, jsonify, request
from services.skill_gap_analyzer import analyze_skill_gap

skill_gap_bp = Blueprint(
    "skill_gap",
    __name__
)

@skill_gap_bp.route("/skill-gap", methods=["GET", "POST"])
def skill_gap():

    if request.method == "POST" and request.is_json:
        user_skills = request.json.get("skills", [])
        target_role = request.json.get("career", "AI Engineer")
    else:
        skills_param = request.args.get("skills", "")
        user_skills = [s.strip() for s in skills_param.split(",") if s.strip()]
        target_role = request.args.get("career", "AI Engineer")

    missing_skills = analyze_skill_gap(user_skills, target_role)

    return jsonify({
        "career": target_role,
        "missing_skills": missing_skills
    })
