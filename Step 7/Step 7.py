# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

txt = " "
with Image.open("oxygen.png") as img:
    pix = img.load()
    width, height = img.size
    i = 0
    while i < width-21:
        txt += chr((pix[i, height/2][0]))
        i += 7
    print(txt)

solutionCoded = [105, 110, 116, 101, 103, 114, 105, 116, 121]
solutionDecoded = [chr(x) for x in solutionCoded]
print(solutionDecoded)
