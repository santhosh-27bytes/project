import PyPDF2

def extract_resume_text(path):

    text = ""

    with open(path, "rb") as file:

        pdf = PyPDF2.PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()

    return text