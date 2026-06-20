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

    file = request.files["resume"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    return jsonify({
        "message": "Resume uploaded",
        "file": file.filename
    })