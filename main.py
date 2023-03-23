from fpdf import FPDF
import pandas as pd

file = pd.read_csv("topics.csv")

pdf = FPDF(orientation="L", unit="mm", format="A4")
for index, row in file.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=40)
    pdf.set_text_color(50,0,245)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(10, 24, 200, 22)
    for j in range(row["Pages"]):
        pdf.add_page()

pdf.output("output.pdf")