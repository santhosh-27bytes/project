from flask import Blueprint, jsonify
from services.skill_gap_analyzer import analyze_skill_gap

skill_gap_bp = Blueprint(
    "skill_gap",
    __name__
)

@skill_gap_bp.route("/skill-gap")
def skill_gap():

    return jsonify({

        "missing_skills":[
            "Deep Learning",
            "MLOps",
            "Statistics",
            "System Design"
        ]

    })