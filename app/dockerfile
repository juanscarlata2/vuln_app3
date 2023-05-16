# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos requeridos al directorio de trabajo
COPY requirements.txt ./
COPY app.py ./

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo flag.txt y establece los permisos de lectura
COPY flag.txt ./
RUN chmod 444 flag.txt

# Crea un usuario no root para ejecutar la aplicación
RUN useradd -m webu
USER webu

# Expone el puerto 5000 en el contenedor
EXPOSE 5000

# Ejecuta la aplicación Flask cuando el contenedor se inicie
ENV FLASK_ENV=production
CMD [ "python", "app.py" ]
