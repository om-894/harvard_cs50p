

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# list of fonts
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2]) # set font to 3rd element in list.

else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text)) # This is how you output the text in the font using pyfiglet module.

