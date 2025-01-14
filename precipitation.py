import json
import csv
res = {}
#from collections import defaultdict
#from datetime import datetime

with open ('stations.csv') as file:
    stations= list(csv.DictReader (file))
print (stations)


with open ('precipitation.json',encoding='utf-8') as file:
    contents= json.load(file)
#print (contents)

precipitation_info ={}


#Seattle data
seattle_station = 'GHCND:US1WAKG0038'
Seattle_state= "WA"
city_name = "Seattle"
seattle_data= []


for station in stations:
    #city_data
    station_number = station['Station']
    state= station['State']
    city_name= station['Location']
    city_data =[] #LISTTT
    for measurement in contents:
        if (measurement['station']) == seattle_station:
            seattle_data.append(measurement)
    #print (seattle_data)



    #seattle monthly precipitation
    total_monthly_precipitation= {}

    for measurement in seattle_data:
        month= (int(measurement['date'].split('-')[1]))
        precipitation = measurement['value']
        if month in total_monthly_precipitation:
            total_monthly_precipitation[month] += precipitation
        else:
            total_monthly_precipitation [month]= 0
            
    #print(total_monthly_precipitation)


    #seattle yearly precipitation
    total_yearly_precipitation= sum(total_monthly_precipitation.values())
    #print(total_yearly_precipitation)

    #relative_monthly_precipitation
    relative_monthly_precipitation = {}
    for month in total_monthly_precipitation:
        relative_monthly_precipitation[month] = (
            total_monthly_precipitation[month] / total_yearly_precipitation
        )
#print(relative_monthly_precipitation)



    precipitation_info[city_name] = {
        'station': station_number,
        'state':state,
        'total_monthly_precipitation': list(total_monthly_precipitation.values()),
        'total_yearly_precipitation': total_yearly_precipitation,
        'relative_monthly_precipitation': list(relative_monthly_precipitation.values())
        }  

with open ('results.json', 'w') as file:
    json.dump(precipitation_info,file,indent=4)








 




        



