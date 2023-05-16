# vuln_app3
Una app vulnerable para pruebas


## Instalación
Clonar el repo

crear la imagen de docker

```sudo docker build -t myapp --network=host .```

Ejecutar el contenedor

```docker run -p 5000:5000 myapp```
