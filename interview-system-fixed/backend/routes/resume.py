from flask import Blueprint, request, jsonify
from services.resume_analyzer import (
    extract_resume_text,
    extract_skills
)
import os

resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads"

@resume_bp.route("/upload-resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    try:
        text = extract_resume_text(filepath)
        skills = extract_skills(text)
    except Exception as e:
        return jsonify({
            "error": f"Could not analyze resume: {str(e)}"
        }), 500

    return jsonify({
        "message": "Resume uploaded and analyzed",
        "file": file.filename,
        "skills": skills
    })
