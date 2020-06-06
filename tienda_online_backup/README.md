# Tienda online

# Dependencias
+ python3
+ python3-django

# El directorio "tienda_online_vistas" es el cuerpo de la aplicación

# Para ejecutar el servidor en local ejecute los siguientes comandos
+ cd tienda_online
+ python manage.py runserver

# Creamos un nuevo proyecto en django
django-admin startproject NOMBRE-DEL-PROYECTO

# Crear una nueva aplicación
python manage.py startapp NOMBRE-APLICACION

# Inicializa el servidor
python manage.py runserver

# Genera una base de datos vacía
python manage.py makemigrations

# Django genera el código sql en la base de datos vacía
python manage.py sqlmigrate NOMBRE-APP NUMERO-MIGRACION

# Implementa la nueva base de datos en django
python manage.py migrate
