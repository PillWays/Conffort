from django.db import models

# Create your models here.

# Diseño de la base de datos "registro_usuario()",
# por defecto utiliza "sqlite", para el registro de usuarios
# se debe indicar en django que "models.py" es una aplicación
# eso se registra en el archivo "/tienda_online/tienda_online/settings.py"
# la base de datos se guarda en "./db.sqlite3"

class registro_usuario(models.Model):
	nombre_usuario=models.CharField(max_length=80)
	email_usuario=models.EmailField(max_length=80)
	password_usuario=models.CharField(max_length=80)
