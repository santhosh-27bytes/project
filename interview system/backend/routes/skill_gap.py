from flask import Blueprint, jsonify

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