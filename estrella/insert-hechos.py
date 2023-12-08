import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="estrella"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Inicializar la lista de datos de hechos
datos_hechos = []

# Generar automáticamente 20 conjuntos de datos para la Tabla de Hechos
for i in range(1, 21):
    datos_hechos.append((i, i, i, i, i, float(i) * 10, f'Metricas {chr(ord("A") + i - 1)}'))

# Sentencia SQL para insertar datos en la Tabla de Hechos
sql_insert_hechos = """
    INSERT INTO TablaHechos (id_transaccion, id_ubicacion, id_producto, id_cliente, id_tiempo, venta_total, metricas_asociadas)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Insertar datos en la Tabla de Hechos
for dato in datos_hechos:
    cursor.execute(sql_insert_hechos, dato)

# Confirmar la transacción y cerrar la conexión
conexion.commit()

# Mostrar los resultados después de los inserts
consulta_select = "SELECT * FROM TablaHechos;"
cursor.execute(consulta_select)
resultados = cursor.fetchall()

print("\nDatos en la Tabla de Hechos después de los inserts:")
for resultado in resultados:
    print(resultado)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
