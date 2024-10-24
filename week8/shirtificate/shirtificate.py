from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def header(self):

        self.set_font("helvetica", "B", 50)
        self.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", x=10, y=70, w=self.epw)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(0, 10, f"{self.name} took CS50", align="C")

def main():
    name = input("name")
    pdf = PDF(name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")

main()


#check50 cs50/problems/2022/python/shirtificate


