from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Amilcar")
print(result)

result_suma_dos_numeros = client.service.SumaDosNumeros(num1=10, num2=20)
print("Suma de dos números:", result_suma_dos_numeros)

result_cadena_palindromo = client.service.CadenaPalindromo(cadena="reconocer")
print("¿Es palíndromo?:", result_cadena_palindromo)