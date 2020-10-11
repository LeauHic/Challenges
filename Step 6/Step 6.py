# http://www.pythonchallenge.com/pc/def/channel.html
# Here, the challenge is to find the zip...
# Consider the zip as a zip directory not as the zip method from python.
# if you're looking for a zip file, it is only a matter of extension...






























# Solution : replace html by zip in the url and you can download the zip file
# Now with the readme, we can go through the zip file by searching the correct file
# From the zipfile library we will need 3 things :
# zipFile.read(filename) --> read the content of the filename (byte format by default)
# zipFile.getInfo  --> Generate a ZipInfo object from the file
# zipInfo.comment --> Return the associated comment from the ZipInfo object (byte format by default)

import re
import zipfile

# Create a zipFile instance of the zip file
file = zipfile.ZipFile("D:\Programation\Python\Projets\Enigme\Step 6\channel.zip")
# Hint of the readme.txt
PARAM = "90052"
comments = ''

while True:
    # Reading the file (byte format by default --> needs to be decoded)
    content = file.read(PARAM + ".txt").decode()
    # Getting a zipInfo object with zipFile.getInfo
    info = file.getinfo(PARAM + ".txt")
    # Collecting the comment from the zipInfo (byte format by default --> needs to be decoded)
    comments += info.comment.decode()
    listContent = content.split(" ")
    PARAM = listContent[len(listContent)-1]

    # If the param is not a digit we break the loop and display the comments
    if re.search(r"\d+", PARAM) is None:
        print(comments)
        break
