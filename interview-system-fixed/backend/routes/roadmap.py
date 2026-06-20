from flask import Blueprint
from flask import jsonify, request
from services.roadmap_generator import generate_roadmap


roadmap_bp = Blueprint(
    "roadmap",
    __name__
)

@roadmap_bp.route("/roadmap")
def roadmap():

    career = request.args.get("career", "AI Engineer")

    result = generate_roadmap(career)

    if not result:
        return jsonify({
            "error": f"No roadmap available for '{career}'"
        }), 404

    return jsonify(result)
