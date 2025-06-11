# Imagen oficial de Python, se usa "slim" porque es mas pequeña
FROM python:3.10-slim-buster

# Dentro del contenedor establecemos el directorio de trabajo
# Acá se van a copiar mis archivos y se EJECUTA LA APPPPP
WORKDIR /app

# Acá se copia el archivo de requisitos a directorio
# Lo hacemos antes de instalar las dependencias para aprovechar el caché de Docker
# Docker va construyendo imágenes capa por capa asi que si no cambió nada desde la 
    # última instrucción, docker usa la capa cacheada. Por eso también esto va ANTES
    # de RUN
COPY requirements.txt .

# Acá se instalan las dependencias
# El no-cache-dir es porque no necesitamos que se guarden los paquetes
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la app al directorio de trabajo
COPY . . 

# Expone el puerto en el que la aplicación Flask va a escuchar
# Flask usa por defecto 5000
EXPOSE 5000
#o sea que este contenedor escucha en el puerto 5000

# El comando para iniciar la aplicación cuando el contenedor se ejecute
CMD ["python", "main.py"]

