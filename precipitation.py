import json
import csv
res= {}

with open ('precipitation.json',encoding='utf-8') as file:
    contents= json.load(file)

#print (contents)

#station = 'value'


seattle= []
for data in contents:
    if (data['station'] == 'GHCND:US1WAKG0038'):
        print (data)

        



#print(data['station']=='GHCND:US1WAKG0038')
