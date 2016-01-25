
import json

datas = []
with open('resultFinal.json') as data_file:
    for data in data_file:
        datas.append(json.loads(data))
        
names = []
print datas
for hotel in datas:
    if not hotel['name'][0] in names:
        names.append(hotel['name'][0])
        
for name in names:
    print name
    
print len(names)
        