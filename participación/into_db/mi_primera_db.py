import sqlite3

conn = sqlite3.connect("restaurante.db")

#Crear tabla de platos
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    categoria INTEGER NOT NULL);
    """
)
# Insertar datos de PLATOS
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('charquecan', 23, 1)
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('plato paceño', 24, 2)
    """
)

# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
#Crear tabla de mesas
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

# Insertar datos de PLATOS
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (123)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (124)
    """
)

#Consultar datos
print("MESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
    