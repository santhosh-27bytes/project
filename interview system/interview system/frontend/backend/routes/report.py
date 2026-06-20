from flask import Blueprint
from flask import jsonify

report_bp = Blueprint(
    "report",
    __name__
)

@report_bp.route("/report")
def report():

    report_data = {

        "resume_score": 88,
        "career_match": "AI Engineer",
        "skill_alignment": 78,
        "interview_score": 82,
        "placement_readiness": 81

    }

    return jsonify(report_data)