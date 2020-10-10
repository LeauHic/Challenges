from collections import Counter

with open("Etape2.txt", "r") as file:
    text = file.read()

text2 = ""

for index, letter in enumerate(text):
    if letter not in text[:index]:
        if letter not in text[index+1:]:
            text2 += letter
print(text2)
