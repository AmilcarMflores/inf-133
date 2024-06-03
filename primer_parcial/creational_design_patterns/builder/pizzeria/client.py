import requests

url = "http://localhost:8000/pizzas"
headers = {'Content-type': 'application/json'}

# GET /pizzas
# response = requests.get(url)
# print(response.json())

# POST /pizzas (1)
# mi_pizza = {
#     "tamaño": "Grande",
#     "masa": "Delgada",
#     "toppings": ["Jamon", "Queso"]
# }
# response = requests.post(url, json=mi_pizza, headers=headers)
# print(response.json())

# PUT /pizzas/1
# edit_pizza = {
#     "tamaño": "Mediano",
#     "masa": "Gruesa",
#     "toppings": ["Pepperone", "Queso"]
# }
# print("PUT /pizzas/1")
# response = requests.put(url+'/1', json=edit_pizza, headers=headers)
# print(response.json())

# POST /pizzas (2)
# mi_pizza = {
#     "tamaño": "Pequeño",
#     "masa": "Delgada",
#     "toppings": ["Jamon", "Piña"]
# }
# response = requests.post(url, json=mi_pizza, headers=headers)
# print(response.json())

# DELETE /pizzas/1
# response = requests.delete(url + '/2')
# print(response.json())

response = requests.get(url)
print(response.json())