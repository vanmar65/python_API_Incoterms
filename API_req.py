import requests

request = requests.get('http://127.0.0.1:8000/DDP')
print("Incoterms version: ", request.json()["Incoterms"])
print("Incoterms applicable to mode of transport: ", request.json()["mode"])
