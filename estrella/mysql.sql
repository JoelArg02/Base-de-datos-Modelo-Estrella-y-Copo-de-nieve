CREATE DATABASE estrella;
USE estrella;

-- Crear la Dimensión Ubicación
CREATE TABLE DimensionUbicacion (
    id_ubicacion INT PRIMARY KEY,
    nombre_ubicacion VARCHAR(255),
    detalles_geograficos VARCHAR(255)
);

-- Crear la Dimensión Producto
CREATE TABLE DimensionProducto (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(255),
    categorias VARCHAR(255),
    inventario INT,
    caracteristicas VARCHAR(255)
);

-- Crear la Dimensión Cliente
CREATE TABLE DimensionCliente (
    id_cliente INT PRIMARY KEY,
    nombre_cliente VARCHAR(255),
    perfil_cliente VARCHAR(255),
    comportamiento VARCHAR(255),
    preferencias VARCHAR(255)
);

-- Crear la Dimensión Tiempo
CREATE TABLE DimensionTiempo (
    id_tiempo INT PRIMARY KEY,
    fecha DATE,
    detalles_temporales VARCHAR(255)
);

-- Crear la Tabla de Hechos
CREATE TABLE TablaHechos (
    id_transaccion INT PRIMARY KEY,
    id_ubicacion INT,
    id_producto INT,
    id_cliente INT,
    id_tiempo INT,
    venta_total DECIMAL(10, 2),
    metricas_asociadas VARCHAR(255),
    FOREIGN KEY (id_ubicacion) REFERENCES DimensionUbicacion(id_ubicacion),
    FOREIGN KEY (id_producto) REFERENCES DimensionProducto(id_producto),
    FOREIGN KEY (id_cliente) REFERENCES DimensionCliente(id_cliente),
    FOREIGN KEY (id_tiempo) REFERENCES DimensionTiempo(id_tiempo)
);