# Replicación MySQL con Docker

Este repositorio proporciona un ejemplo de configuración para la replicación MySQL utilizando contenedores Docker. Se incluyen dos configuraciones: `estrella` y `copo`.

## Configuración Estrella

### Crear la red de Docker

```bash
docker network create estrella

### Configurar maestro

docker run --name estrella-mysql-master -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=1 --memory=700m --storage-opt size=1g mysql:latest --default-authentication-plugin=mysql_native_password
docker network connect estrella estrella-mysql-master
docker exec -it estrella-mysql-master mysql -u root -p

En la consola SQL 

SET @@global.server_id = 1;
DROP USER IF EXISTS 'repl'@'%';
CREATE USER 'repl'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'repl';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
UNLOCK TABLES;

Configurar el esclavo

docker run --name estrella-mysql-slave -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect estrella estrella-mysql-slave
docker exec -it estrella-mysql-slave mysql -u root -p

SET @@global.server_id = 2;
CHANGE MASTER TO MASTER_HOST='estrella-mysql-master', MASTER_USER='repl', MASTER_PASSWORD='repl', MASTER_LOG_FILE='binlog.000002', MASTER_LOG_POS=1009;
START SLAVE;
SHOW SLAVE STATUS;


### Configuracion Copo 

docker network create copo
Configuración Copo
Crear la red de Docker
bash
Copy code
docker network create copo
Configurar maestro
bash
Copy code
docker run --name copo-mysql-master -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m --storage-opt size=1g mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect copo copo-mysql-master
docker exec -it copo-mysql-master mysql -u root -p
En la consola SQL:

sql
Copy code
SET @@global.server_id = 1;
DROP USER IF EXISTS 'repl'@'%';
CREATE USER 'repl'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'repl';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
UNLOCK TABLES;
Configurar esclavo
bash
Copy code
docker run --name copo-mysql-slave -p 3309:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d --cpus=0.5 --memory=700m mysql:latest --default-authentication-plugin=mysql_native_password --require_secure_transport=OFF
docker network connect copo copo-mysql-slave
docker exec -it copo-mysql-slave mysql -u root -p
En la consola SQL:

sql
Copy code
SET @@global.server_id = 2;
CHANGE MASTER TO MASTER_HOST='copo-mysql-master', MASTER_USER='repl', MASTER_PASSWORD='repl', MASTER_LOG_FILE='binlog.000002', MASTER_LOG_POS=1009;
START SLAVE;
SHOW SLAVE STATUS;
Nota: Asegúrate de adaptar las direcciones IP y nombres de host según sea necesario en tu entorno.