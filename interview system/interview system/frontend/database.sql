
CREATE DATABASE IF NOT EXISTS careerpilot_ai;
USE careerpilot_ai;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    college VARCHAR(150),
    department VARCHAR(100),
    graduation_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE resumes (
    resume_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    file_name VARCHAR(255),
    file_path VARCHAR(500),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE user_skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    skill_level ENUM('Beginner','Intermediate','Advanced') DEFAULT 'Beginner',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    project_name VARCHAR(255),
    project_description TEXT,
    technologies TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE careers (
    career_id INT AUTO_INCREMENT PRIMARY KEY,
    career_name VARCHAR(100) UNIQUE,
    description TEXT
);

CREATE TABLE career_required_skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    career_id INT NOT NULL,
    skill_name VARCHAR(100),
    importance_weight FLOAT DEFAULT 1,
    FOREIGN KEY (career_id) REFERENCES careers(career_id) ON DELETE CASCADE
);

CREATE TABLE career_matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_id INT NOT NULL,
    match_percentage FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (career_id) REFERENCES careers(career_id) ON DELETE CASCADE
);

CREATE TABLE skill_gaps (
    gap_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_id INT NOT NULL,
    missing_skill VARCHAR(100),
    priority_level ENUM('Low','Medium','High') DEFAULT 'Medium',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (career_id) REFERENCES careers(career_id) ON DELETE CASCADE
);

CREATE TABLE interview_questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    career_id INT,
    difficulty ENUM('Easy','Medium','Hard'),
    question TEXT,
    FOREIGN KEY (career_id) REFERENCES careers(career_id) ON DELETE SET NULL
);

CREATE TABLE interview_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    technical_score FLOAT DEFAULT 0,
    communication_score FLOAT DEFAULT 0,
    confidence_score FLOAT DEFAULT 0,
    overall_score FLOAT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE placement_readiness (
    readiness_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    readiness_score FLOAT,
    readiness_level VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE learning_roadmaps (
    roadmap_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_id INT NOT NULL,
    roadmap_title VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (career_id) REFERENCES careers(career_id) ON DELETE CASCADE
);

CREATE TABLE roadmap_steps (
    step_id INT AUTO_INCREMENT PRIMARY KEY,
    roadmap_id INT NOT NULL,
    step_order INT,
    title VARCHAR(255),
    description TEXT,
    estimated_weeks INT,
    FOREIGN KEY (roadmap_id) REFERENCES learning_roadmaps(roadmap_id) ON DELETE CASCADE
);

CREATE TABLE learning_resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(100),
    resource_title VARCHAR(255),
    resource_type VARCHAR(50),
    resource_link VARCHAR(500)
);

CREATE TABLE ai_feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    strengths TEXT,
    weaknesses TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO careers(career_name,description) VALUES
('AI Engineer','Build AI and ML solutions'),
('Data Analyst','Analyze and visualize data'),
('Software Engineer','Develop software applications');
