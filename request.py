import json
import requests

'''
response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=4c510e72')
#response = requests.get("https://www.google.com")

if response.status_code == 200:
    print("Conexion exitosa con la API")
    print('-------------------------------')
    data = response.json()
    print(data)
elif response.status_code == 404:
    print("No se pude conectar")
else:
    print("No se pudo conectar o recoletar datos")
'''
#data = {'title': 'value1', 'year': 'value2','plot': 'value3', "Response":"value4"}
params = {'t':'american pie'}
response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=4c510e72', params=params)
#response = requests.get("https://www.google.com")

if response.status_code == 200:
    print("Conexion exitosa con la API")
    print('-------------------------------')
    data = response.json()
    print(response.json())
    print('-------------------------------')
elif response.status_code == 404:
    print("No se pude conectar")
else:
    print("No se pudo conectar o recoletar datos")


"""""
def new_func(response):
    print(response.json())

new_func(response)

"""""