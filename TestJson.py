import json
data = {'A':123, 'B':456, 'C':789}
with open('data.json', 'w') as fw:
    json.dump(data, fw)
