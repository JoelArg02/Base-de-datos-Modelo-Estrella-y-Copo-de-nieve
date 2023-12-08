SELECT
    TH.id_transaccion,
    DU.nombre_ubicacion,
    DP.nombre_producto,
    DM.nombre_marca,
    DIP.inventario,
    DC.nombre_cliente,
    DT.fecha,
    TH.venta_total,
    TH.metricas_asociadas
FROM
    TablaHechos TH
INNER JOIN DimensionUbicacion DU ON TH.id_ubicacion = DU.id_ubicacion
INNER JOIN DimensionProducto DP ON TH.id_producto = DP.id_producto
INNER JOIN DimensionMarcaProducto DM ON DP.id_marca = DM.id_marca
INNER JOIN DimensionInventarioProducto DIP ON DP.id_inventario = DIP.id_inventario
INNER JOIN DimensionCliente DC ON TH.id_cliente = DC.id_cliente
INNER JOIN DimensionTiempo DT ON TH.id_tiempo = DT.id_tiempo;

SELECT
    DP.id_producto,
    DP.nombre_producto,
    DM.nombre_marca,
    DIP.inventario
FROM
    DimensionProducto DP
INNER JOIN DimensionMarcaProducto DM ON DP.id_marca = DM.id_marca
INNER JOIN DimensionInventarioProducto DIP ON DP.id_inventario = DIP.id_inventario;
