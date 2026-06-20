from services.resume_analyzer import extract_resume_text

@resume_bp.route("/analyze-resume", methods=["POST"])
def analyze_resume():

    file = request.files["resume"]

    filepath = "uploads/" + file.filename

    file.save(filepath)

    text = extract_resume_text(filepath)

    return jsonify({
        "resume_text": text[:500]
    })