# https://cs50.harvard.edu/python/2022/psets/4/figlet/

# To tyle bo nie jestem do końca pewny o co chodzi w poleceniu

from pyfiglet import Figlet

figlet = Figlet()

user_input = input('Text: ').strip()

print(figlet.renderText(user_input))