import requests

url = 'http://localhost:8000/graphql'
#Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
  mutation{
    crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biología"){
      estudiante{
        id
        nombre
        apellido
        carrera
      }
    }
  }  
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)