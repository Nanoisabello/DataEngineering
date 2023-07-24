import requests

#response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=4c510e72")
resVar = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=4c510e72",params={"title":"the&mission"})


def new_func(resVar):
    print(resVar.json())

new_func(resVar)