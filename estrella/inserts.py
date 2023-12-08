import mysql.connector
from faker import Faker
from datetime import datetime, timedelta

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="estrella"
)

cursor = conexion.cursor()

fake = Faker('es_ES')

num_registros = 20 

for i in range(1, num_registros + 1):
    nombre_ubicacion = fake.city()
    detalles_geograficos = fake.address()

    consulta_insert = "INSERT INTO DimensionUbicacion (id_ubicacion, nombre_ubicacion, detalles_geograficos) VALUES (%s, %s, %s);"
    

    valores = (i, nombre_ubicacion, detalles_geograficos)


    cursor.execute(consulta_insert, valores)

for i in range(1, num_registros + 1):
    nombre_producto = fake.word()
    categorias = fake.word()
    inventario = fake.random_int(1, 100)
    caracteristicas = fake.text()

    consulta_insert = "INSERT INTO DimensionProducto (id_producto, nombre_producto, categorias, inventario, caracteristicas) VALUES (%s, %s, %s, %s, %s);"
    
    valores = (i, nombre_producto, categorias, inventario, caracteristicas)

    cursor.execute(consulta_insert, valores)

for i in range(1, num_registros + 1):
    nombre_cliente = fake.name()
    perfil_cliente = fake.word()
    comportamiento = fake.word()
    preferencias = fake.text()

    consulta_insert = "INSERT INTO DimensionCliente (id_cliente, nombre_cliente, perfil_cliente, comportamiento, preferencias) VALUES (%s, %s, %s, %s, %s);"
    

    valores = (i, nombre_cliente, perfil_cliente, comportamiento, preferencias)


    cursor.execute(consulta_insert, valores)

for i in range(1, num_registros + 1):
    fecha = fake.date_between(start_date='-30d', end_date='today')
    detalles_temporales = fake.text()


    consulta_insert = "INSERT INTO DimensionTiempo (id_tiempo, fecha, detalles_temporales) VALUES (%s, %s, %s);"
    

    valores = (i, fecha, detalles_temporales)


    cursor.execute(consulta_insert, valores)

conexion.commit()

cursor.close()
conexion.close()
