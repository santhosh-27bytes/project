def analyze_skill_gap(
        user_skills,
        target_role
):

    role_skills = {

        "AI Engineer": [

            "Python",
            "Machine Learning",
            "Deep Learning",
            "MLOps",
            "Statistics"

        ],

        "Data Analyst": [

            "Python",
            "SQL",
            "Statistics"

        ]

    }

    required_skills = role_skills.get(
        target_role,
        []
    )

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:

            missing_skills.append(skill)

    return missing_skills