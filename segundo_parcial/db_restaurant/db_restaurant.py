import sqlite3

conn = sqlite3.connect("restaurante.db")

# Crear la tabla platos
try:
  conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL);
    """
  )
except sqlite3.OperationalError:
  print("Ya fue creada la tabla PLATOS")
  
# Insertamos datos en la tabla PLATOS
# conn.execute(
#   """
#   INSERT INTO PLATOS (nombre, precio, categoria)
#   VALUES ('Pizza', 10.99, 'Italiana')
#   """
# )  
# conn.execute(
#   """
#   INSERT INTO PLATOS (nombre, precio, categoria)
#   VALUES ('Hamburguesa', 8.99, 'Americana')
#   """
# )
# conn.execute(
#   """
#   INSERT INTO PLATOS (nombre, precio, categoria)
#   VALUES ('Sushi', 12.99, 'Japonesa')
#   """
# )
# conn.execute(
#   """
#   INSERT INTO PLATOS (nombre, precio, categoria)
#   VALUES ('Ensalada', 6.99, 'Vegetariana')
#   """
# )
# Crear la tabla mesas
try:
  conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
  )
except sqlite3.OperationalError:
  print("Ya fue creada la tabla MESAS")
  
# Insertamos datos a la tabla mesas
# conn.execute(
#   """
#   INSERT INTO MESAS (numero)
#   VALUES (1)
#   """
# )  
# conn.execute(
#   """
#   INSERT INTO MESAS (numero)
#   VALUES (2)
#   """
# )
# conn.execute(
#   """
#   INSERT INTO MESAS (numero)
#   VALUES (3)
#   """
# )
# conn.execute(
#   """
#   INSERT INTO MESAS (numero)
#   VALUES (4)
#   """
# )
  
# Crear la tabla pedidos
try:
  conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
  )
except sqlite3.OperationalError:
  print("Ya fue creada la tabla PEDIDOS")
  
# Insertamos datos en la tabla pedidos
# conn.execute(
#   """
#   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
#   VALUES (1, 2, 2, '2024-04-01')
#   """
# )  
# conn.execute(
#   """
#   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
#   VALUES (2, 3, 1, '2024-04-01')
#   """
# )  
# conn.execute(
#   """
#   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
#   VALUES (3, 1, 3, '2024-04-02')
#   """
# )
# conn.execute(
#   """
#   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
#   VALUES (4, 4, 1, '2024-04-02')
#   """
# )

# Actualiza el precio del plato con id 2 (Hamburguesa) a 9.99
conn.execute(
  """
  UPDATE PLATOS 
  SET precio = 9.99
  WHERE id = 2
  """
)

# Cambia la categoría del plato con id 3 (Sushi) a "Fusión"
conn.execute(
  """
  UPDATE PLATOS
  SET categoria = 'Fusión'
  WHERE id = 3
  """
)

# Elimina el pedido con id 3
conn.execute(
  """
  DELETE FROM PEDIDOS
  WHERE id = 3
  """
)

# Confirmar cambios 
conn.commit()

# Cerrar la conexión
conn.close()