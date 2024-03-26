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

# PUT /pizzas/1
actualizar_ruta = url + "/1"
edit_pizza = {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Queso"]
}
response = requests.put(url = actualizar_ruta, json=edit_pizza, headers=headers)
print(response.json())


# DELETE /pizzas/1
response = requests.delete(url + "/1")
print(response.json())

