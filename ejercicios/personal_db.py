import sqlite3

#conectar 
conn = sqlite3.connect("personal.db")

#Crea tabla DEPARTAMENTOS
try:
    conn.execute(
    """
    CREATE TABLE DEPARTAMENTOS(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL
    );
    """
    )
except sqlite3.OperationalError:
    print("Ya fue creada la tabla DEPARTAMENTOS")

#insertar DEPARTAMENTOS
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Ventas', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Marketing', '11-04-2020')
    """
)

#Crear tabla CARGOS
try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla ya fue creada de DEPARTAMENTOS")    

#insertar CARGOS
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Gerente de Ventas', 'Senior', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Anallista de Marketing', 'Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Representante de Ventas', 'Junior', '12-04-2020')
    """
)

#Crear tabla EMPLEADOS
try:
    conn.execute(
    """
    CREATE TABLE EMPLEADOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    apellido_materno TEXT NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento_id INTEGER NOT NULL,
    cargo_id INTEGER NOT NULL,
    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
    FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
    """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya fue creada")


 #Insertar EMPLEADOS
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('Juan', 'Gonzáles', 'Pérez', '15-05-2023', 1, 1)
    """
)   
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('María', 'López', 'Martínez', '20-06-2023', 2, 2)
    """
)


#crear tabla salarios
try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya fue creada...")

#Insertar datos SALARIOS
conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin)
    VALUES (1, 3000, '01-04-2024', '30-04-2024')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin)
    VALUES (2, 3500, '01-07-2024', '30-04-2024')
    """
)

#María López Martínez renunció
#Elimina sus registro de la base de datos
# conn.execute(
#     """
    
#     DELETE FROM EMPLEADOS INNER SALARIOS
#     WHERE nombre = 'María' AND apellido_paterno = 'López' AND apellido_materno = 'Martínez'

#     """
# )

# print("\nEMPLEADOS:")
# cursor = conn.execute(
#     "SELECT * FROM EMPLEADOS"
# )

# for row in cursor:
#     print(row)

conn.commit()

conn.close()

