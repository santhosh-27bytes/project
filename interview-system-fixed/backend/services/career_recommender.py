def recommend_career(skills):

    careers = {

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning"
        ],

        "Data Analyst": [
            "Python",
            "SQL"
        ],

        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript"
        ]

    }

    results = {}

    for career, required_skills in careers.items():

        match_count = 0

        for skill in required_skills:

            if skill in skills:
                match_count += 1

        score = int(
            (match_count / len(required_skills))
            * 100
        )

        results[career] = score

    return results