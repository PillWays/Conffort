# Se agregó el metodo "HttpResponse" para ejecutar
# las peticiones de los usuarios
from django.shortcuts import render, HttpResponse

# Clases y metodos utilizados para manejar 
# el envío de emails  
from django.core.mail import send_mail
from django.conf import settings

# Importamos las tablas del diseño de la base de datos
# ubicada en el archivo "./models.py"
from tienda_online_vistas.models import registro_usuario

# Create your views here.

# La fución "inicio(request)" renderiza la página de inicio
def inicio(request):
	return render(request, "Conffort/index.html")

# La función "registro(request)" inserta los datos a la base de datos,
# renderica la página de registro y la página del login 
def registro(request):

	# Comprueba si en el formulario de registro se envían datos
	# y direcciona a la página de login cuando se registra el usuario,
	# de no ser así se mantiene en la página de registro	
	if request.method=="POST":

		# Captura los datos ingresados en el formulario de registro
		nombre_usuario_fm=request.POST["nombre-usuario"]
		email_usuario_fm=request.POST["email-usuario"]
		password_usuario_fm=request.POST["password-usuario"]

		# Inserta los datos capturados en los formularios en la base de datos
		registro_db=registro_usuario(
			nombre_usuario=nombre_usuario_fm,
			email_usuario=email_usuario_fm,
			password_usuario=password_usuario_fm
		)

		# Guardamos los datos insertados en la base de datos
		registro_db.save()

		return render(request, "Conffort/iniciar_sesion.html",)

	return render(request, "Conffort/registro.html")

# La función "iniciar_sesion(request)" valída si el email y el password coiniciden
# con el almacenado en la base de datos, de ser así, direcciona a la página de catalogo
# y muestra el nombre de usuario en el navbar, de no ser así se mantiene en la página de login
def inicio_sesion(request):

	# Comprueba si el usuario envía datos desde el formulario de login
	if request.method=="POST":

		# Captura los datos ingresados en el formulario de login
		email_usuario_login=request.POST["email-usuario-login"]
		password_usuario_login=request.POST["password-usuario-login"]


		# Filtra si el correo y el password coincide con el de la base de datos
		nombre_consulta_db=registro_usuario.objects.filter(email_usuario__exact=email_usuario_login, password_usuario__exact=password_usuario_login)

		# Comprueba si el usuario existe
		if nombre_consulta_db:
			navbar_catalogo={"nombre_login":nombre_consulta_db[0].nombre_usuario, "id_user":nombre_consulta_db[0].id}
			return render(request, "Conffort/catalogo.html", navbar_catalogo)

	return render(request, "Conffort/iniciar_sesion.html") 

# La función "email(request)" se encarga de envía emails,
# el usuario envía un mensaje de contacto al correo oficial del sitio,
# y el servidor le contesta con un correo de mensaje envíado
def email(request):

	# Comprueba si el usuario envía datos desde el formulario email
	if request.method=="POST":
		
		# Captura los datos ingresados en el formulario email
		email_usuario=request.POST["contactMail"]
		email_usuario_list=[email_usuario]		

		mensaje=request.POST["textoEmail"] + '\n' + 'Atte: ' + email_usuario
		asunto='Contacto Conffort'
		email_sitio=settings.EMAIL_HOST_USER
		
		# Lista de correos donde llegaran los mensajes envíados por los usuarios
		email_contacto_sitio=[email_sitio]
		
		# Envia el correo a a la dirección email del sitio
		send_mail(asunto,mensaje,email_sitio,email_contacto_sitio)

		# Envía un correo de confirmación de envío al usuario
		mensaje_respuesta='Pronto contactaremos con usted\n' + 'Atte: ' + email_sitio
		send_mail(asunto, mensaje_respuesta, email_sitio, email_usuario_list)

	return render(request,"Conffort/index.html")


# La función "borrar(request,id_user)" elimina usuario
def borrar(request,id_user):
	
	# Desde el inicio de sesión captura el id del usuario, compruba que
	# el botón sea pulsado, de no ser así se mantiene en la página de catalogo
	if request.method=="POST":
		borrar_usuario=registro_usuario.objects.get(id=id_user)
		borrar_usuario.delete()
		return render(request, "Conffort/index.html")
		
	return render(request,"Conffort/catalogo.html")


