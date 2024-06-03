import requests

url = "http://localhost:8000/player/"
headers = {"Content-Type": "application/json"}

response = requests.request(method="GET", url=url)
print(response.text)

damage_value = 10
data = {"damage": damage_value}
response = requests.post(url=url + "damage", json=data, headers=headers)

if response.status_code  == 200:
  print("Estado del jugador:", response.json())
else:
  print("Error al aplicar daño:", response.text())