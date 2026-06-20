from flask import Blueprint
from flask import jsonify

report_bp = Blueprint(
    "report",
    __name__
)

@report_bp.route("/report")
def report():

    return jsonify({

        "resume_score":88,
        "career":"AI Engineer",
        "alignment":78,
        "interview":82,
        "readiness":81

    })