from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet


def generate_resume_grade_pdf(data, filename="resume_grade_report.pdf"):
    extracted_name = data.get("name", "Not Provided")
    extracted_email = data.get("email", "Not Provided")
    extracted_education = data.get("education", "Not Provided")
    overall_comment = data.get("overall_comment", "No comment provided.")

    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph("Resume Evaluation Report", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Candidate Details
    name = Paragraph(f"<b>Name:</b> {extracted_name}", styles["BodyText"])
    email = Paragraph(f"<b>Email:</b> {extracted_email}", styles["BodyText"])
    education = Paragraph(
        f"<b>Education:</b> {extracted_education}", styles["BodyText"]
    )

    elements.extend([name, email, education, Spacer(1, 20)])

    # Overall Score
    overall_score = Paragraph(
        f"<b>Overall Score:</b> {data['overall_score']}", styles["Heading2"]
    )
    elements.append(overall_score)
    elements.append(Spacer(1, 10))

    # Overall Comment
    overall_comment_paragraph = Paragraph(
        f"<b>Overall Comment:</b> {overall_comment}", styles["BodyText"]
    )
    elements.append(overall_comment_paragraph)
    elements.append(Spacer(1, 20))

    # Scores and Feedback
    for section, details in data["scores"].items():
        section_header = Paragraph(
            f"<b>{section}:</b> (Score: {details['score']})", styles["Heading3"]
        )
        elements.append(section_header)
        elements.append(Spacer(1, 10))

        feedback_title = Paragraph(
            f"<i>{details['feedback_title']}</i>", styles["BodyText"]
        )
        elements.append(feedback_title)
        elements.append(Spacer(1, 5))

        feedback_text = Paragraph(details["feedback"], styles["BodyText"])
        elements.append(feedback_text)
        elements.append(Spacer(1, 20))

    doc.build(elements)
    print(f"PDF report '{filename}' generated successfully.")
