# Utilizamos la imagen oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /src

# instalar librerias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el script de Python al directorio de trabajo
COPY . .

# Ejecutamos el script de Python
CMD ["python", "main.py"]

#Docker