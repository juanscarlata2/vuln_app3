# vuln_app3
Una app vulnerable para pruebas


## Instalación
Clonar el repo

```cd vuln_app3/app/```

crear la imagen de docker

```docker build -t myapp --network=host .```

Ejecutar el contenedor

```docker run -p 5000:5000 myapp```
