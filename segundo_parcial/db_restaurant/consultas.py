import sqlite3

conn = sqlite3.connect("restaurante.db")

# Encuentra todos los pedidos realizados junto con los nombres de los platos y los números de mesa (JOIN)
print("\nPedidos junto con los nombres de los platos y número de mesa:")
cursor = conn.execute(
  """
  SELECT PEDIDOS.id, PLATOS.nombre, MESAS.numero
  FROM PEDIDOS
  JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id
  JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id 
  """
)
for row in cursor:
  print(row)
  
# Encuentra todos los platos que han sido pedidos, incluso aquellos que no se han pedido aún
print("\nTodos los platos que han sido pedidos, incluso aquellos que no se han pedido aún:")
cursor = conn.execute(
  """
  SELECT PEDIDOS.plato_id, PEDIDOS.cantidad, PLATOS.nombre
  FROM PLATOS
  LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
  """
)  
for row in cursor:
  print(row)
