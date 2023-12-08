import mysql.connector
from faker import Faker
from datetime import datetime, timedelta

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3308,
    database="copo"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crear una instancia de Faker en español
fake = Faker('es_ES')

# Número de registros a insertar
num_registros = 20

# Generar e insertar datos en la tabla DimensionUbicacion
for i in range(1, num_registros + 1):
    nombre_ubicacion = fake.city()
    detalles_geograficos = fake.address()

    # Crear la consulta INSERT
    consulta_insert = "INSERT INTO DimensionUbicacion (id_ubicacion, nombre_ubicacion, detalles_geograficos) VALUES (%s, %s, %s);"
    
    # Valores a insertar
    valores = (i, nombre_ubicacion, detalles_geograficos)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, valores)

#Generar e insertar datos en la tabla DimensionMarcaProducto
for i in range(1, num_registros + 1):
    nombre_marca = fake.company()

    # Crear la consulta INSERT
    consulta_insert = "INSERT INTO DimensionMarcaProducto (id_marca, nombre_marca) VALUES (%s, %s);"
    # Valores a insertar
    valores = (i, nombre_marca)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, valores)


# Generar e insertar datos en la tabla DimensionInventarioProducto
for i in range(1, num_registros + 1):
    inventario = fake.random_int(1, 100)

    consulta_insert = "INSERT INTO DimensionInventarioProducto (id_inventario, inventario) VALUES (%s, %s);"

    valores = (i, inventario,)

    cursor.execute(consulta_insert, valores)


# Generar e insertar datos en la tabla DimensionCliente
for i in range(1, num_registros + 1):
    nombre_cliente = fake.name()
    perfil_cliente = fake.word()
    comportamiento = fake.word()
    preferencias = fake.text()

    # Crear la consulta INSERT
    consulta_insert = "INSERT INTO DimensionCliente (id_cliente, nombre_cliente, perfil_cliente, comportamiento, preferencias) VALUES (%s, %s, %s, %s, %s);"
    
    # Valores a insertar
    valores = (i, nombre_cliente, perfil_cliente, comportamiento, preferencias)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, valores)

# Generar e insertar datos en la tabla DimensionTiempo
for i in range(1, num_registros + 1):
    fecha = fake.date_between(start_date='-30d', end_date='today')
    detalles_temporales = fake.text()

    # Crear la consulta INSERT
    consulta_insert = "INSERT INTO DimensionTiempo (id_tiempo, fecha, detalles_temporales) VALUES (%s, %s, %s);"
    
    # Valores a insertar
    valores = (i, fecha, detalles_temporales)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, valores)

#Generar e insertar datos en la tabla DimensionProducto
for i in range(1, num_registros + 1):
    nombre_producto = fake.word()
    id_marca = i
    id_inventario = i
    # Crear la consulta INSERT
    consulta_insert = "INSERT INTO DimensionProducto (id_producto, nombre_producto, id_marca, id_inventario) VALUES (%s, %s, %s, %s);"
    
    # Valores a insertar
    valores = (i,nombre_producto, id_marca, id_inventario)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, valores)

#Generar e insertar datos en la tabla Hechos
# Generar e insertar datos en la tabla Hechos
for i in range(1, num_registros + 1):
    id_ubicacion = i
    id_producto = i
    id_cliente = i
    id_tiempo = i
    venta_total = fake.random_int(1, 100)
    metricas_asociadas = fake.text()

    consulta_insert = "INSERT INTO TablaHechos (id_transaccion, id_ubicacion, id_producto, id_cliente, id_tiempo, venta_total, metricas_asociadas) VALUES (%s, %s, %s, %s, %s, %s, %s);"

    valores = (i, id_ubicacion, id_producto, id_cliente, id_tiempo, venta_total, metricas_asociadas)

    cursor.execute(consulta_insert, valores)


conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
