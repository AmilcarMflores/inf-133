from zeep import Client

#Instanciamos el cliente
client = Client('http://localhost:8000')

#Llamamos al servicio "Saludar"
result = client.service.Saludar(nombre="Replicant")
print(result)
