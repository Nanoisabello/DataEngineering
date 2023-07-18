import json
import requests

response = requests.get('http://www.omdbapi.com/?apikey=[yourkey]&"')

if response.status_code == 200:
    print("Conexion exitosa con la API")
    print('-------------------------------')
    data = response.json()
    print(data)
elif response.status_code == 404:
    print("No se pude conectar")
else:
    print("No se pudo conectar o recoletar datos")

import requests

data = {'title': 'value1', 'year': 'value2','plot': 'value3', "Response":"value4"}
response = requests.get('http://www.omdbapi.com/?apikey=[yourkey]&"', params=data)

if response.status_code == 200:
    print("Conexion exitosa con la API")
    print('-------------------------------')
    data = response.json()
elif response.status_code == 404:
    print("No se pude conectar")
else:
    print("No se pudo conectar o recoletar datos")")
for record in data:
     print("Title: {},\n Release_Year: {},\n Director: {},\n".format(record['title'] , record['release_Year'],record['director']))
