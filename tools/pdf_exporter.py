from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch, mm
import os
import datetime


def export_pdf(
    report_text: str,
    filename="research_report.pdf",
    title="Generative AI Research Paper",
    author="Anonymous Author, Dept. of AI",
):
    os.makedirs("outputs", exist_ok=True)
    path = os.path.join("outputs", filename)

    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
    )

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="TitleStyle",
        fontSize=16,
        alignment=TA_CENTER,
        spaceAfter=20,
        leading=20,
        fontName="Helvetica-Bold"
    ))

    styles.add(ParagraphStyle(
        name="AuthorStyle",
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=30,
    ))

    styles.add(ParagraphStyle(
        name="AbstractTitle",
        fontSize=11,
        fontName="Helvetica-Bold",
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name="AbstractText",
        fontSize=10,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=20,
        italic=True
    ))

    styles.add(ParagraphStyle(
        name="Section",
        fontSize=11,
        fontName="Helvetica-Bold",
        spaceBefore=12,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name="Body",
        fontSize=10,
        spaceAfter=8,
        leading=14
    ))

    content = []

    # ---------- TITLE PAGE ----------
    content.append(Paragraph(title, styles["TitleStyle"]))
    content.append(Paragraph(author, styles["AuthorStyle"]))
    content.append(Paragraph(
        datetime.datetime.now().strftime("%B %Y"),
        styles["AuthorStyle"]
    ))
    content.append(PageBreak())

    # ---------- PARSE REPORT ----------
    lines = report_text.split("\n")

    in_abstract = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "abstract" in line.lower():
            content.append(Paragraph("Abstract", styles["AbstractTitle"]))
            in_abstract = True
            continue

        if in_abstract and line.lower().startswith(("1.", "i.", "introduction")):
            in_abstract = False

        if in_abstract:
            content.append(Paragraph(line, styles["AbstractText"]))
            continue

        if line.lower().startswith(("1.", "2.", "3.", "4.", "5.", "introduction", "conclusion", "references")):
            content.append(Spacer(1, 12))
            content.append(Paragraph(line, styles["Section"]))
        else:
            content.append(Paragraph(line, styles["Body"]))

    # ---------- PAGE NUMBERING ----------
    def add_page_numbers(canvas, doc):
        page_num = canvas.getPageNumber()
        canvas.drawRightString(200 * mm, 15 * mm, f"{page_num}")

    doc.build(content, onLaterPages=add_page_numbers, onFirstPage=add_page_numbers)

    return path
