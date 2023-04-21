import requests

resource = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('sp_3_6_2.txt') as text:
    curret_resource = text.readline()[len(resource)-1:]

while curret_resource[0:2] != 'We':
    curret_resource = requests.get(resource + curret_resource).text
print(curret_resource)
