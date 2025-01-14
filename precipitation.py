import json
import csv
#from collections import defaultdict
#from datetime import datetime

#the csv file that contains the state, location and station
with open ('stations.csv') as file:
    stations= list(csv.DictReader (file))
#print (stations)


with open ('precipitation.json',encoding='utf-8') as file:
    contents= json.load(file)
#print (contents)

precipitation_info ={}
total_precipitation_all_stations = 0       #startit with 0

#keep everything in the loop 
for station in stations:                #loop over the state stations (keep it all in loop)
    #city_data
    station_number = station['Station']
    state= station['State']                         #CASE SENSITIVEEEEEE
    city_name= station['Location']
    city_data =[] #LISTTT
    for measurements in contents:
        if (measurements['station']) == station_number:
            city_data.append(measurements)
    #print (seattle_data)



    #seattle monthly precipitation
    total_monthly_precipitation= {}

    for measurements in city_data:
        month= (int(measurements['date'].split('-')[1]))   #list of strings that are now integers 
        precipitation = measurements['value']              #that are split by the dash in the date
        if month in total_monthly_precipitation:           #use the first index since python starts on 0
            total_monthly_precipitation[month] += precipitation
        else:
            total_monthly_precipitation [month]= 0
            
    #print(total_monthly_precipitation)


    #yearly precipitation for one station THEN ALL STATIONS
    total_yearly_precipitation= sum(total_monthly_precipitation.values())
    total_precipitation_all_stations += total_yearly_precipitation       #add the values of each month tog
    #print(total_yearly_precipitation)

    #relative_monthly_precipitation
    relative_monthly_precipitation = {}
    for month in total_monthly_precipitation:
        relative_monthly_precipitation[month] = (
            total_monthly_precipitation[month] / total_yearly_precipitation
        )  #if total precipitation of all months is 100%...how much is one month????
#print(relative_monthly_precipitation)



    precipitation_info[city_name] = {
        'station': station_number,
        'state':state,
        'total_monthly_precipitation': list(total_monthly_precipitation.values()), #MAKE A LISSST 
        'total_yearly_precipitation': total_yearly_precipitation,
        'relative_monthly_precipitation': list(relative_monthly_precipitation.values())
        }  

#get the relative precipitation of each state compared to the total precipitation yearly
for city_name, data in precipitation_info.items():
    data['relative_yearly_precipitation'] = (
        data['total_yearly_precipitation'] / total_precipitation_all_stations
    )   #this should be outside the loop 

with open ('results.json', 'w') as file:
    json.dump(precipitation_info,file,indent=4)








 




        



