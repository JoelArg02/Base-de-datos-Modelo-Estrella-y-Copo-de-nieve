SELECT
    TH.id_transaccion,
    DU.nombre_ubicacion,
    DP.nombre_producto,
    DC.nombre_cliente,
    DT.fecha,
    TH.venta_total,
    TH.metricas_asociadas
FROM
    TablaHechos TH
JOIN
    DimensionUbicacion DU ON TH.id_ubicacion = DU.id_ubicacion
JOIN
    DimensionProducto DP ON TH.id_producto = DP.id_producto
JOIN
    DimensionCliente DC ON TH.id_cliente = DC.id_cliente
JOIN
    DimensionTiempo DT ON TH.id_tiempo = DT.id_tiempo;
