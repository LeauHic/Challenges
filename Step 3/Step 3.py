# http://www.pythonchallenge.com/pc/def/equality.html
# Looking for exactly 3 upper-case letters, 1 lower-case letter, 3 upper-case letter
# With re.findall, with find every match to the regular expression --> return a list of tuple /
# tuple structure : (1 letter before, the match, 1 letter after)
# scan the list and for every tuple get the 4th letter of the 2 elements

import re

with open("Step 3_Source.txt", "r") as file:
    text = file.read()

text2 = ""

m = re.findall(r"([a-z])([A-Z]{3}[a-z][A-Z]{3})([a-z])", text)
for res in m:
    text2 += res[1][3]

print(text2)
print(m)
