import requests

url = "http://localhost:8000/pizzas"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())
