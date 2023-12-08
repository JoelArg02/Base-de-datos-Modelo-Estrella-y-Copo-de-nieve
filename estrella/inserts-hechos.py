import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="estrella"
)
cursor = conexion.cursor()
datos_hechos = []
for i in range(1, 21):
    datos_hechos.append((i, i, i, i, i, float(i) * 10, f'Metricas {chr(ord("A") + i - 1)}'))
sql_insert_hechos = """
    INSERT INTO TablaHechos (id_transaccion, id_ubicacion, id_producto, id_cliente, id_tiempo, venta_total, metricas_asociadas)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for dato in datos_hechos:
    cursor.execute(sql_insert_hechos, dato)

conexion.commit()

consulta_select = "SELECT * FROM TablaHechos;"
cursor.execute(consulta_select)
resultados = cursor.fetchall()

print("\nDatos en la Tabla de Hechos después de los inserts:")
for resultado in resultados:
    print(resultado)

cursor.close()
conexion.close()
