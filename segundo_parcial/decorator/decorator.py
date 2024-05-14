# functools --> proporciona funciones para trabajar con funciones y objetos llamables (callable objects).

# wraps --> la función wraps se utiliza comúnmente en el contexto de definir decoradores
from functools import wraps

def my_decorator(func):
  # Usamos wraps para preservar los metadatos de la función original
  @wraps(func)
  def wrapper(*args, **kwargs):
    print("Antes de llamar a la función")
    # Llamamos a la función original con sus argumentos y guardamos el resultado
    # Adicionalmente convertimos la cadena en mayúscula
    result = func(*args, **kwargs).upper()
    
    print("Después de llamar a la función")
    return result
  return wrapper

# Aplica el decorador a una función
@my_decorator
def greet(name):
  """Función para saludar a alguien"""
  return f'¡Hola, {name}!'
  
print(greet("Juan"))

# Conserva el nombre original de la función
print(greet.__name__)
# Conserva la cadena de documentación original de la función
print(greet.__doc__)