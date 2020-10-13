# http://www.pythonchallenge.com/pc/def/integrity.html

# The module Bz2 allow to archive files / to decompress archives or files
# The decompression of files is allowed is the files are in binary format.

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

pwDecompressed = bz2.decompress(pw)
unDecompressed = bz2.decompress(un)
print("Username : {}\nPassword : {}".format(unDecompressed.decode(), pwDecompressed.decode()))


