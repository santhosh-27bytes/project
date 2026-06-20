from flask import Blueprint
from flask import jsonify

roadmap_bp = Blueprint(
    "roadmap",
    __name__
)

@roadmap_bp.route("/roadmap")
def roadmap():

    return jsonify({

        "month1":[
            "Python",
            "Statistics"
        ],

        "month2":[
            "Machine Learning",
            "SQL"
        ],

        "month3":[
            "Deep Learning"
        ]

    })