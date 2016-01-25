import json
datas = []
with open('resultFinal.json') as data_file:
    for data in data_file:
        datas.append(json.loads(data))
        

#print datas
