import requests

PARAM = "12345"
URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
table = []
for i in range(0, 399):
    with requests.get(url=URL+PARAM) as r:
        data = r.text
        listData = data.split(" ")
        lenListData = len(listData)
        PARAM = listData[lenListData-1]
        table.append(r.text)

print(table)
