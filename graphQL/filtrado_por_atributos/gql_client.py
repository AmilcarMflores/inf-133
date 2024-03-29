import requests

#Definir la consulta GraphQL con parámetros
query = """
    {
      estudiantePorId(id:2){
        nombre
      }
    }
"""
#Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

#Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)