Alphabet = "abcdefghijklmnopqrstuvwxyz"
Ralphabet = "cdefghijklmnopqrstuvwxyzab"
TextCoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
            "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
            "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"
print(TextCoded.translate(str.maketrans(Alphabet, Ralphabet)))
print(url.translate(str.maketrans(Alphabet, Ralphabet)))
