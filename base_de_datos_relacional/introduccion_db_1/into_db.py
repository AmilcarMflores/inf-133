# Importar módulo sqlite3
import sqlite3

# Iniciando la DB
# Crear conexión a la base de datos
conn = sqlite3.connect("instituto.db")

#Creando una tabla
# Crear tabla de carreras
try:
  conn.execute(
  """
  CREATE TABLE CARRERAS
  (id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  duracion INTEGER NOT NULL);
  """
  )
except sqlite3.OperationalError:
  print("La tabla CARRERAS ya existe")

#Insertar datos de carreras
conn.execute(
  """
  INSERT INTO CARRERAS(nombre, duracion)
  VALUES('Ingeniería en Informática', 5)
  """
)
conn.execute(
  """
  INSERT INTO CARRERAS(nombre, duracion)
  VALUES('Licenciatura en Administración', 4)
  """
)

#Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
  print(row)

# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4) 

#Crear tablas de estudiantes
try:
  conn.execute(
  """
  CREATE TABLE ESTUDIANTES
  (id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  fecha_nacimiento DATE NOT NULL);
  """
  )
except sqlite3.OperationalError:
  print("La tabla ESTUDIANTES ya existe")

#Insertar datos de estudiantes
conn.execute(
  """
  INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
  VALUES ('Juan', 'Pérez', '2000-05-15')
  """
)
conn.execute(
  """
  INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
  VALUES ('María', 'Lopez', '1999-08-20')
  """
)

#Consultar datos de estudiantes
print("\nEstudiantes:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
  print(row)
  
# Estudiantes:
# (1, 'Juan', 'Pérez', '2000-05-15')      
# (2, 'María', 'Lopez', '1999-08-20')  

#Crear tabla de matriculación
try:
  conn.execute(
  """
  CREATE TABLE MATRICULACION
  (id INTEGER PRIMARY KEY,
  estudiante_id INTEGER NOT NULL,
  carrera_id INTEGER NOT NULL,
  fecha TEXT NOT NULL,
  FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
  FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
  """
  )
except sqlite3.OperationalError:
  print("La tabla MATRICULACIÓN ya existe")

#Insertar datos de matriculación
conn.execute(
  """
  INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
  VALUES (1, 1, '2024-01-15')
  """
)
conn.execute(
  """
  INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
  VALUES (2, 2, '2024-01-20')
  """
)
conn.execute(
  """
  INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
  VALUES (1, 2, '2024-01-25')
  """
)

#Consultar datos de matriculación
print("\nMatriculación:")
cursor = conn.execute(
  """
  SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha
  FROM MATRICULACION
  JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
  JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
  """
)
for row in cursor:
  print(row)
  
# Matriculación:
# ('Juan', 'Pérez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Pérez', 'Licenciatura en Administración', '2024-01-25')  

#Listar datos de matriculación
print("\Matriculación:")
cursor = conn.execute(
  "SELECT * FROM MATRICULACION"
)
for row in cursor:
  print(row)
  
# \Matriculación:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')
# (3, 1, 2, '2024-01-25')

#Actualizar una fila de la tabla de matriculación
conn.execute(
  """
  UPDATE MATRICULACION
  SET fecha = '2024-01-30'
  WHERE id = 2
  """
)

#Listar datos de matriculación
print("\nMATRICULACIÓN:")
cursor = conn.execute(
  "SELECT * FROM MATRICULACION"
)
for row in cursor:
  print(row)
  
# MATRICULACIÓN:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')
# (3, 1, 2, '2024-01-25')


#Confirmar cambios
conn.commit()

#Cerrar conexión
conn.close()