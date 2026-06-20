from reportlab.pdfgen import canvas

def create_report(filepath):

    pdf = canvas.Canvas(filepath)

    pdf.drawString(
        100,
        800,
        "CareerPilot AI Report"
    )

    pdf.drawString(
        100,
        760,
        "Resume Score: 88"
    )

    pdf.drawString(
        100,
        740,
        "Career Match: AI Engineer"
    )

    pdf.drawString(
        100,
        720,
        "Placement Readiness: 81%"
    )

    pdf.save()