# En el archivo db_restaurant.py hicimos todas las operaciones, peros esto siempre ha sido un problema ya que la sintaxis se hace muy extensa y como humanos nos es difícil poder ubicar algo en concreto a la hora de modificar, crear o eliminar.
# Para más organización y eficiencia trabajaremos en este archivo:
import sqlite3

conn = sqlite3.connect("instituto.db")

# conn.execute(
#   """
#   INSERT INTO ESTUDIANTES (nombre, apellido_paterno, fecha_nacimiento)
#   VALUES ('Carlos', 'Gomez', '2001-02-10')
#   """
# )

# conn.execute(
#   """
#   INSERT INTO CARRERAS (nombre, duracion)
#   VALUES ('Licenciatura en Contabilidad', 4)
#   """
# )

# INNER JOIN O JOIN
print("\nINNER JOIN O JOIN: ")
cursor = conn.execute(
  """
  SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido_paterno, CARRERAS.nombre, MATRICULACION.fecha
  FROM MATRICULACION
  JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
  JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
  """
)
for row in cursor:
  print(row)

# LEFT JOIN
print("\nLEFT JOIN:")
cursor = conn.execute(
  """
  SELECT CARRERAS.nombre, ESTUDIANTES.nombre
  FROM CARRERAS
  LEFT JOIN MATRICULACION ON CARRERAS.id = MATRICULACION.carrera_id
  LEFT JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
  """
)
for row in cursor:
  print(row)

# RIGHT JOIN
print("\nRIGHT JOIN:")
cursor = conn.execute(
  """
  SELECT ESTUDIANTES.nombre, CARRERAS.nombre
  FROM ESTUDIANTES
  RIGHT JOIN MATRICULACION ON ESTUDIANTES.id = MATRICULACION.estudiante_id
  RIGHT JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
  """
)
for row in cursor:
  print(row)

# Confirmar cambios 
conn.commit()

# Cerrar conexión
conn.close()