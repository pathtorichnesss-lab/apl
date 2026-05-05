from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import re

doc = SimpleDocTemplate(
    "/home/user/apl/posts/pathtorichnesss-all-posts.pdf",
    pagesize=A4,
    rightMargin=20*mm,
    leftMargin=20*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
)

purple = colors.HexColor("#7B4FA6")
light_purple = colors.HexColor("#B39DDB")
dark = colors.HexColor("#2A2A2A")
muted = colors.HexColor("#888888")

styles = getSampleStyleSheet()

title_style = ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=18,
    textColor=purple, spaceAfter=6, spaceBefore=14, alignment=TA_LEFT)
post_header_style = ParagraphStyle("PostHeader", fontName="Helvetica-Bold", fontSize=12,
    textColor=light_purple, spaceAfter=4, spaceBefore=12, alignment=TA_LEFT)
body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=10.5,
    textColor=dark, spaceAfter=3, leading=16, alignment=TA_LEFT)

SKIP_PREFIXES = (
    "Written", "Product:", "What it", "Price:", "Discount:", "Link:",
    "Three versions", "10 posts", "20 more", "8 more", "15 more",
    "Wide variety", "6 posts", "Mix", "Copy-paste", "Styles:",
    "Different", "Inspired", "All in", "No bot", "Not polished",
)

def clean(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.strip()

story = []

# Cover
story.append(Spacer(1, 30*mm))
story.append(Paragraph("@pathtorichnesss", ParagraphStyle("Cover", fontName="Helvetica-Bold",
    fontSize=28, textColor=purple, alignment=TA_CENTER)))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("Content Posts — All In One", ParagraphStyle("CoverSub",
    fontName="Helvetica", fontSize=13, textColor=light_purple, alignment=TA_CENTER)))
story.append(Spacer(1, 8*mm))
story.append(HRFlowable(width="100%", thickness=1, color=light_purple))
story.append(Spacer(1, 60*mm))
story.append(Paragraph("Personal Growth • APL Promos • Win Posts",
    ParagraphStyle("CoverTag", fontName="Helvetica", fontSize=11,
    textColor=muted, alignment=TA_CENTER)))

with open("/home/user/apl/posts/all-posts-combined.md", "r") as f:
    lines = f.readlines()

for line in lines:
    stripped = line.strip()

    if stripped.startswith("# ") and not stripped.startswith("## "):
        story.append(Spacer(1, 4*mm))
        story.append(HRFlowable(width="100%", thickness=0.5, color=light_purple))
        story.append(Paragraph(clean(stripped[2:]), title_style))

    elif stripped.startswith("## "):
        story.append(Paragraph(clean(stripped[3:]), post_header_style))

    elif stripped == "---":
        story.append(Spacer(1, 2*mm))
        story.append(HRFlowable(width="100%", thickness=0.3, color=colors.HexColor("#E0D6F0")))
        story.append(Spacer(1, 2*mm))

    elif stripped == "":
        story.append(Spacer(1, 2*mm))

    elif any(stripped.startswith(p) for p in SKIP_PREFIXES):
        continue

    else:
        story.append(Paragraph(clean(stripped), body_style))

doc.build(story)
print("PDF created successfully")
