import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()

if len(sys.argv) == 1:
    font = figlet.setFont(font = random.choice(font_list))
elif len(sys.argv) == 3:
    if sys.argv[1] == ("-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
        font = figlet.setFont(font = sys.argv[2])

    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

print(figlet.renderText(input("input:")))


