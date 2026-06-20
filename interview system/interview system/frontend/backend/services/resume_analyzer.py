import PyPDF2

def extract_resume_text(filepath):

    text = ""

    with open(filepath, "rb") as file:

        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


def extract_skills(text):

    skills_db = [

        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "React"

    ]

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills