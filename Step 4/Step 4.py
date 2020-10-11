# http://www.pythonchallenge.com/pc/def/linkedlist.php
# with the get method from the request library, we can get the result of the url
# with the re library, we can check if the the last piece of the returned sentence is a number or not

# starting with 123456, will return an indication to restart with another parameter divided by two

import requests
import re

# PARAM = "12345"
PARAM = str(16044/2)

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
table = []

for i in range(0, 400):
    with requests.get(url=URL+PARAM) as r:
        data = r.text
        listData = data.split(" ")
        if re.match(r"\d+", PARAM) is None:
            # print(data) ##To get the complete text displayed
            print(PARAM)
            break
        PARAM = listData[len(listData) - 1]
