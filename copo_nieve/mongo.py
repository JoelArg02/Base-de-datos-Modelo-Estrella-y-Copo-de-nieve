import mysql.connector
import pymongo
from datetime import datetime, timedelta
from decimal import Decimal


# MySQL Connection
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3308,
    database="copo"  # Update with your new database name
)
mysql_cursor = mysql_connection.cursor(dictionary=True)

# MongoDB Connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["copo"]  # Update with your new MongoDB database name

# Fetch data from MySQL and insert into MongoDB

mysql_cursor.execute("SELECT * FROM DimensionUbicacion")
ubicaciones = mysql_cursor.fetchall()
ubicacion_collection = mongo_db["DimensionUbicacion"]
ubicacion_collection.insert_many(ubicaciones)

mysql_cursor.execute("SELECT * FROM DimensionMarcaProducto")
marcas = mysql_cursor.fetchall()
marca_collection = mongo_db["DimensionMarcaProducto"]
marca_collection.insert_many(marcas)

mysql_cursor.execute("SELECT * FROM DimensionInventarioProducto")
inventarios = mysql_cursor.fetchall()
inventario_collection = mongo_db["DimensionInventarioProducto"]
inventario_collection.insert_many(inventarios)

mysql_cursor.execute("SELECT * FROM DimensionProducto")
productos = mysql_cursor.fetchall()
producto_collection = mongo_db["DimensionProducto"]
producto_collection.insert_many(productos)

mysql_cursor.execute("SELECT * FROM DimensionCliente")
clientes = mysql_cursor.fetchall()
cliente_collection = mongo_db["DimensionCliente"]
cliente_collection.insert_many(clientes)

mysql_cursor.execute("SELECT * FROM DimensionTiempo")
tiempos = mysql_cursor.fetchall()
tiempo_collection = mongo_db["DimensionTiempo"]
for tiempo in tiempos:
    tiempo['fecha'] = datetime(tiempo['fecha'].year, tiempo['fecha'].month, tiempo['fecha'].day)
tiempo_collection.insert_many(tiempos)

mysql_cursor.execute("SELECT * FROM TablaHechos")
hechos = mysql_cursor.fetchall()
hechos_collection = mongo_db["TablaHechos"]
for hecho in hechos:
    hecho['venta_total'] = float(hecho['venta_total'])
hechos_collection.insert_many(hechos)

# Close connections
mysql_cursor.close()
mysql_connection.close()
mongo_client.close()
