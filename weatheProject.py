import requests
import json, os, csv
import pandas as pad
from pathlib import Path
import numpy as num 

res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=apparent_temperature')
file = res.json()['hourly']

fcsv = pad.DataFrame.from_dict(file).to_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv', index=False)

df = pad.read_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv')

for i in df['time']:
    df['time'].replace(i, i[:10], inplace=True)
    
df.to_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv', index=False)

fileTemp = {}
value = []
for i in range(1, len(df['time'])):
    if df['time'][i] != df['time'][i-1]:
        fileTemp[df['time'][i-1] ] = value
        value = []
    elif i+1 == len(df['time']):
        value.append(df['apparent_temperature'][i])  
        fileTemp[df['time'][i] ] = value
        break 
    else:
        value.append(df['apparent_temperature'][i-1])   

fcsv = pad.DataFrame.from_dict(fileTemp).to_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv', index=False)

df = pad.read_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv')

for i in fileTemp.keys():
    df[i+'mean'] = df[i].mean()
    
df.to_csv('c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv', index=False)

poke = pad.read_csv("c:/Users/liliz/OneDrive\Documenti\python/weather/weathercopy.csv")
print(poke)