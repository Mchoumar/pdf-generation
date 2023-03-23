from fpdf import FPDF
import pandas as pd

file = pd.read_csv("topics.csv")

pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in file.iterrows():
    # set the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=40)
    pdf.set_text_color(50, 0, 245)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    for i in range(20, 298, 10):
        pdf.line(10, i, 285, i)

    pdf.ln(165)

    # set the footer
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for j in range(row["Pages"]):
        pdf.add_page()
        for i in range(20, 298, 10):
            pdf.line(10, i, 285, i)

        # set the footer
        pdf.ln(175)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")