import pickle
content = b''
with open('SourceCodeDosFormat.p', 'rb') as file:
    content = file.read()

stringContent = content.decode('ASCII')
listContent = stringContent.split("\r")
with open('test', 'wb') as file:
    newContent = b''
    for line in listContent:
        newContent += line.encode('ASCII')
    file.write(newContent)


with open('SourceCodeUnixFormat', 'rb') as file:
    DecodedFile = pickle.load(file)
#    print(DecodedFile)
    for index,Tuple in enumerate(DecodedFile):
        secretCode = ''
        for subliste in Tuple:
            secretCode += subliste[0] * subliste[1]
        print(secretCode)
