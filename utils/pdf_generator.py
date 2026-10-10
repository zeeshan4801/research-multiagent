from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from io import BytesIO



def create_pdf(content):

    buffer = BytesIO()


    doc = SimpleDocTemplate(
        buffer,
        title="AI Research Report"
    )


    styles = getSampleStyleSheet()


    story = []


    for line in content.split("\n"):

        story.append(

            Paragraph(
                line,
                styles["BodyText"]
            )

        )

        story.append(
            Spacer(1,12)
        )


    doc.build(story)


    buffer.seek(0)


    return buffer
