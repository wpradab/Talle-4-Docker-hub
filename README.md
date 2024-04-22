
# Taller de Docker y FastAPI

## Descripción
Este taller fue desarrollado por William David Prada Buitrago, Juan David Torres Jimenez, y Ricardo Macias Bohorquez. El objetivo era crear una imagen de Docker que contenga una API utilizando FastAPI para realizar inferencias con un modelo previamente entrenado y publicar la imagen final en Docker Hub para su uso y prueba usando Locust.

## Requerimientos
- Docker
- Docker Compose
- FastAPI
- Locust para pruebas de carga

## Instrucciones para usar el repositorio
El modelo que se usó para este trabajo fue el clasificador de especies de pingüinos.
1. **Levantar el Docker Compose para la API del modelo de pingüinos**

   Descargue el repositorio.
   ```bash
   git clone https://github.com/wpradab/Talle-4-Docker-hub.git
   ```

   Para iniciar la API, use el Docker Compose desde el repositorio con el siguiente comando:
   ```bash
   docker-compose -d up
   ```
   Esto cargará la imagen del Docker Hub y levantará el servicio.

3. **Levantar el Docker Compose para Locust**
   Para ejecutar las pruebas de carga con Locust, use el Docker Compose en la carpeta `locust` del repositorio. Ejecute el siguiente comando para iniciar Locust:
   ```bash
   docker-compose -f locust/docker-compose.yaml up
   ```

   Una vez que Locust esté ejecutándose, puede acceder a la interfaz web para las pruebas de carga en:
   [http://localhost:8089](http://localhost:8089)

4. **Verificar que la API del modelo esté activa**
   Con el servicio de la API ejecutándose, puede acceder a la documentación de la API en:
   [http://localhost:8000/docs](http://localhost:8000/docs)

5. **Correr en Locust para pruebas de carga**
   Después de levantar la interfaz web para las pruebas de carga, se debe verificar que la petición se haga a [http://mi-servicio](http://mi-servicio) (Nombre del contenedor del modelo), luego ejecutar las pruebas de carga dando al botón RUN.

## Resultados de las pruebas de carga
La siguiente imagen muestra los resultados de las pruebas de carga, donde se alcanzaron 10,000 usuarios.
![total_requests_per_second_1713752480 097 (1)](https://github.com/wpradab/Talle-4-Docker-hub/assets/142359246/3bbf2729-37be-4d62-ae07-2fe2ef5bdf1a)


## Referencias
- [Repositorio del proyecto en GitHub](https://github.com/wpradab/Talle-4-Docker-hub.git)
- [Imagen de Docker Hub](https://hub.docker.com/r/david984/penguin_inference)
