def generate_roadmap(career):

    roadmaps = {

        "AI Engineer": {

            "Month 1": [
                "Python",
                "Statistics"
            ],

            "Month 2": [
                "Machine Learning",
                "SQL"
            ],

            "Month 3": [
                "Deep Learning"
            ],

            "Month 4": [
                "MLOps"
            ],

            "Month 5": [
                "Projects"
            ],

            "Month 6": [
                "Interview Preparation"
            ]
        }
    }

    return roadmaps.get(
        career,
        {}
    )