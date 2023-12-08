# Replicación MySQL con Docker

Este repositorio proporciona un ejemplo de configuración para la replicación MySQL utilizando contenedores Docker. Se incluyen dos configuraciones: `estrella` y `copo`.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado Docker en tu sistema. Puedes descargar Docker desde [https://www.docker.com/get-started](https://www.docker.com/get-started).

## Configuración Estrella
### Crear la red de Docker

```bash
docker network create estrella
```
### Configurar maestro

```cmd
docker run --name estrella-mysql-master -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=1 --memory=700m --storage-opt size=1g mysql:latest --default-authentication-plugin=mysql_native_password
docker network connect estrella estrella-mysql-master
docker exec -it estrella-mysql-master mysql -u root -p
```
### En la consola SQL 

```sql
SET @@global.server_id = 1;
DROP USER IF EXISTS 'repl'@'%';
CREATE USER 'repl'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'repl';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```

### No olvides desbloquear las tablas

```sql
UNLOCK TABLES;
```
### Configurar el esclavo
```cmd
docker run --name estrella-mysql-slave -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect estrella estrella-mysql-slave
docker exec -it estrella-mysql-slave mysql -u root -p
```
```sql
SET @@global.server_id = 2;
CHANGE MASTER TO MASTER_HOST='estrella-mysql-master', MASTER_USER='repl', MASTER_PASSWORD='repl', MASTER_LOG_FILE='binlog.000002', MASTER_LOG_POS=1009;
START SLAVE;
SHOW SLAVE STATUS;
```

## Configuracion Copo 

```CMD
docker network create copo

```
### Configurar maestro
```
docker run --name copo-mysql-master -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m --storage-opt size=1g mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect copo copo-mysql-master
docker exec -it copo-mysql-master mysql -u root -p
```

```sql
SET @@global.server_id = 1;
DROP USER IF EXISTS 'repl'@'%';
CREATE USER 'repl'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'repl';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```
## Configurar esclavo
```bash
docker run --name copo-mysql-slave -p 3309:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect copo copo-mysql-slave
docker exec -it copo-mysql-slave mysql -u root -p
```
## En la consola SQL:
```sql
SET @@global.server_id = 2;
CHANGE MASTER TO MASTER_HOST='copo-mysql-master', MASTER_USER='repl', MASTER_PASSWORD='repl', MASTER_LOG_FILE='binlog.000002', MASTER_LOG_POS=1009;
START SLAVE;
SHOW SLAVE STATUS;
```
### No olvides desbloquear las tablas una vez realizada el slave
```sql
UNLOCK TABLES;
```
Nota: Asegúrate de adaptar las direcciones IP y nombres de host según sea necesario en tu entorno.