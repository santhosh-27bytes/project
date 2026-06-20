from flask import Blueprint
from flask import jsonify, send_file
import os
from services.pdf_generator import create_report

report_bp = Blueprint(
    "report",
    __name__
)

REPORT_FOLDER = "reports"

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


@report_bp.route("/report/download")
def download_report():

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    filepath = os.path.join(REPORT_FOLDER, "CareerPilot_Report.pdf")

    create_report(filepath)

    return send_file(
        filepath,
        as_attachment=True,
        download_name="CareerPilot_Report.pdf",
        mimetype="application/pdf"
    )
