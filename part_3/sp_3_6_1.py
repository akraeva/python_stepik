import requests

file_name = 'sp_3_6_1.txt'
with open(file_name) as text:
    resource_name = text.readline().strip()

text = requests.get(resource_name).text

result = len(text.splitlines())
print(result)
