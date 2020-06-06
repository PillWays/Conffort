from django.urls import path
from tienda_online_vistas import views

urlpatterns = [
	path('', views.inicio, name="inicio-url"),
	path('registro', views.registro, name="registro-url"),
	path('login', views.inicio_sesion, name="login-url"),
	path('enviado_email', views.email, name="email-url"),
	path('delete_user/<int:id_user>',views.borrar, name="delete-user-url"),
]

