
# Taller de Docker y FastAPI

## Descripción
Este taller fue desarrollado por William David Prada Buitrago, Juan David Torres Jimenez, y Ricardo Macias Bohorquez. El objetivo era crear una imagen de Docker que contenga una API utilizando FastAPI para realizar inferencias con un modelo previamente entrenado. El modelo se consume directamente desde FastAPI, y la imagen final se publica en Docker Hub para su uso.

## Requerimientos
- Docker
- Docker Compose
- FastAPI
- Locust para pruebas de carga

## Instrucciones para usar la imagen de Docker
1. **Descargar la imagen de Docker desde Docker Hub**
   ```bash
   docker pull david984/penguin_inference
   ```

2. **Ejecutar la imagen con Docker Compose**
   Para ejecutar la imagen de inferencia con Docker Compose, use el siguiente archivo `docker-compose.yaml`:
   ```yaml
   version: '3.8'
   services:
     mi-servicio:
       image: david984/penguin_inference:latest
       ports:
         - "8000:80"
       networks:
         - locust_network
       deploy:
         resources:
           limits:
             cpus: '2'
             memory: 1024M
   networks:
     locust_network:
       external: true
   ```

   Para iniciar el servicio, ejecute:
   ```bash
   docker-compose up
   ```

3. **Probar la API**
   Con el servicio ejecutándose, puede acceder a la documentación de la API en:
   [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Realizar pruebas de carga con Locust**
   Para realizar pruebas de carga, use el siguiente archivo `docker-compose.yaml` para Locust:
   ```yaml
   version: '3.7'
   services:
     locust-master:
       image: locustio/locust
       ports:
         - "8089:8089"
       volumes:
         - ./locustfile.py:/mnt/locust/locustfile.py
       command: -f /mnt/locust/locustfile.py --master -H http://mi-servicio
       networks:
         - locust_network
     locust-worker:
       image: locustio/locust
       volumes:
         - ./locustfile.py:/mnt/locust/locustfile.py
       command: -f /mnt/locust/locustfile.py --worker --master-host locust-master
       networks:
         - locust_network
   networks:
     locust_network:
       external: true
   ```

   Luego, ejecute:
   ```bash
   docker-compose -f locust/docker-compose.yaml up
   ```

   Una vez que Locust esté ejecutándose, puede acceder a la interfaz web para las pruebas de carga en:
   [http://localhost:8089](http://localhost:8089)

## Resultados de las pruebas de carga
La siguiente imágen muestra los resultados de las pruebas de carga, donde se alcanzaron 10,000 usuarios.

![Resultados](C:/Users/rmaci/Downloads/10000request.png)


## Referencias
- [Imagen de Docker Hub](https://hub.docker.com/r/david984/penguin_inference)
