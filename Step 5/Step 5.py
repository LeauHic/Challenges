# The pickle library allows to serialize, deserialize a text at the UNIX format
# UNIX format : "next line" indication = \n
# DOS format : next line indication = \r

import pickle

# The file get from the website "banner.p" is on the DOS format,so the first step is to convert it into UNIX format
content = ''
with open('SourceCodeDosFormat.p', 'r') as file:
    content = file.read()

# We get the content from the file, transforms it into list separated by "\r"
listContent = content.split("\r")

# We write into a new file in binary (pickle works only on binary file)
with open('test', 'wb') as file:
    newContent = b''
    for line in listContent:
        # The string.encode() method allow to convert a string into binary (utf-8 by default)
        newContent += line.encode()
    file.write(newContent)

# Now we can pickle the file
with open('SourceCodeUnixFormat', 'rb') as file:
    DecodedFile = pickle.load(file)
#    print(DecodedFile) --> The file is a list of list of tuples
    # For every list in the main list
    for sublist in DecodedFile:
        secretCode = ''
        for Tuple in sublist:
            # Print the character ' ' or '#' the number of times indicated int the second part of the tuple
            secretCode += Tuple[0] * Tuple[1]
        print(secretCode)
