from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(summary, actions, filename):

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Meeting Assistant Report", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Summary:", styles['Heading2']))
    content.append(Spacer(1, 10))

    for line in summary.split("."):
        content.append(Paragraph(line.strip(), styles['Normal']))
        content.append(Spacer(1, 8))

    content.append(Spacer(1, 20))
    content.append(Paragraph("Action Items:", styles['Heading2']))
    content.append(Spacer(1, 10))

    for action in actions:
        content.append(Paragraph(action, styles['Normal']))
        content.append(Spacer(1, 8))

    doc.build(content)
