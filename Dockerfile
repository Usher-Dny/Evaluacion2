# Usa una imagen base de Python oficial
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu carpeta actual al contenedor
COPY . /app

# Instala Flask para que la aplicación funcione
RUN pip install flask

# REQUERIMIENTO: El puerto solicitado es el 7777 
EXPOSE 7777

# Comando para iniciar tu script
CMD ["python", "Daniel_G.py"]
