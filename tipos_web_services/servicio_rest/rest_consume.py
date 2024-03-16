#Importamos el cliente
import requests

#Declaramos la URL del servicio
card_number = "BT1-010"
url = f"https://digimoncard.io/api-public/search.php?card={card_number}"

#Consumimos el servicio 
response = requests.request(
  method="GET",
  url=url,
  headers={"Content-Type": "application/json"},
  data={}
)
print(response.text)