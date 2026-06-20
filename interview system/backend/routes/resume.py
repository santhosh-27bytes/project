from flask import Blueprint, request, jsonify
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