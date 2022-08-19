import json

with open('data.json', 'r') as fr:
    data = json.load(fr)
    print(data)

