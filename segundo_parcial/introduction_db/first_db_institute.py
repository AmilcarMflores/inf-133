# Importar módulo sqlite3
import sqlite3

# INICIANDO LA DB
# Crear conexión a la base de datos
conn = sqlite3.connect("instituto.db")

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

# Insertar datos de carrera
conn.execute(
  """
  INSERT INTO CARRERAS (nombre, duracion)
  VALUES ('Ingeniería de Informática', 5)
  """
)
conn.execute(
  """
  INSERT INTO CARRERAS (nombre, duracion)
  VALUES ('Licenciatura de Administración', 4)
  """
)

# Consultar datos de carreras
print("\nCARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
  print(row)
  
# Crear tabla de estudiantes
try:
  conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
  )
except sqlite3.OperationalError:
  print("Ya fue creado la tabla ESTUDIANTES")
  
# Insertar datos de estudiantes
conn.execute(
  """
  INSERT INTO ESTUDIANTES(nombre, apellido_paterno, fecha_nacimiento)
  VALUES ('Juan', 'Perez', '2000-05-15')
  """
)
conn.execute(
  """
  INSERT INTO ESTUDIANTES(nombre, apellido_paterno, fecha_nacimiento)
  VALUES ('María', 'Lopez', '1999-08-20')
  """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
  print(row)

# Crear tabla para matriculación
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
  print("Ya fue creado la tabla MATRICULACIÓN")
  
# Insertar datos de matriculación
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

# Listar datos de matriculación
print("\nMATRICULACIÓN:")
cursor = conn.execute("SELECT * FROM MATRICULACION")
for row in cursor:
  print(row)
  
# Consultar datos de matriculación
print("\nConsultar datos:")
print("MATRICULACIÓN:")
cursor = conn.execute(
  """
  SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido_paterno, CARRERAS.nombre, MATRICULACION.fecha FROM MATRICULACION
  JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
  JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
  """
)
for row in cursor:
  print(row)

# Confirmar cambios 
conn.commit()

# Cerrar conexión
conn.close()
