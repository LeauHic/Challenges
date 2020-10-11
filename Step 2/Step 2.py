# http://www.pythonchallenge.com/pc/def/ocr.html
# Get the content of the file withe the open, and read method
# reading characters by characters, if it doesn't appear before and after, it is a single character

with open("Step 2_source.txt", "r") as file:
    text = file.read()

text2 = ""

for index, letter in enumerate(text):
    if letter not in text[:index] and letter not in text[index+1:]:
        text2 += letter
print(text2)
