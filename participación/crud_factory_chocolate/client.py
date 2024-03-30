import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

#GET
response = requests.get(url=url)
print(response.json())

#POST
new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": "20kg",
    "sabor": "vainilla"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "bombon",
    "peso": "40kg",
    "sabor": "chocolate blanco",
    "relleno": "manjar de chocolate"
    
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

#PUT
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "25kg"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

#DELETE
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())