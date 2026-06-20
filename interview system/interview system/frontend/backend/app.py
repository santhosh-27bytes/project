from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.resume import resume_bp
from routes.career_match import career_bp
from routes.skill_gap import skill_gap_bp
from routes.interview import interview_bp
from routes.roadmap import roadmap_bp
from routes.report import report_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(career_bp)
app.register_blueprint(skill_gap_bp)
app.register_blueprint(interview_bp)
app.register_blueprint(roadmap_bp)
app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run(debug=True)