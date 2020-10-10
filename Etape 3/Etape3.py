import re

with open("Etape3.txt", "r") as file:
    text = file.read()

text2 = ""

m = re.findall(r"([a-z])([A-Z]{3}[a-z][A-Z]{3})([a-z])", text)
for res in m:
    text2 += res[1][3]

print(text2)
