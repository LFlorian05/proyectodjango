from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
	path('libros/', views.listar_libros, name='listar_libros'),
	path('libros/crear/', views.crear_libro, name='crear_libro'),
	path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
	path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),]

if settings.DEBUG:
    urlpatterns+= static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)