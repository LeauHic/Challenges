# http://www.pythonchallenge.com/pc/def/map.html
# using 2 methods form the string class :
#  - string.translate(table)
#  ==> transform a string to another, using the translation table in argument.
#  - string.maketrans("input", "output")
#  ==> create a translation table from 2 strings : the input and the expected result in output.

Alphabet = "abcdefghijklmnopqrstuvwxyz"

Ralphabet = "cdefghijklmnopqrstuvwxyzab"

TextCoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
            "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
            "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "map"
print(TextCoded.translate(str.maketrans(Alphabet, Ralphabet)))
print(url.translate(str.maketrans(Alphabet, Ralphabet)))
