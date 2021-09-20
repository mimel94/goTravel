"""gotravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from apps.controlUsuarios.views import Login, CrearUsuario, logout_usuario, Dashboard
from apps.sitios.views import CrearSitio, ListarSitiosPropios, ActualizarSitio, Index, MostrarSitio, crearComentario, ListarComentarios, Puntuacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(), name='index'),

    path('crearUsuario/', CrearUsuario.as_view(), name='crear_usuario'),    
    path("accounts/login/",Login.as_view(),name='login'),
    path("logout/",login_required(logout_usuario), name="logout"),
    path("dashboard/",Dashboard.as_view(),name="dashboard"),

    path("dashboard/crear-sitio/",CrearSitio.as_view(),name="crear_sitio"),
    path("dashboard/listar-sitios/",ListarSitiosPropios.as_view(),name="listar_sitios_propios"),
    path("dashboard/actualizar-sitio/<int:pk>/",ActualizarSitio.as_view(),name="actualizar_sitio"),

    path("web/detalle-sitio/<int:pk>/",MostrarSitio.as_view(), name="detalle_sitio_publico"),
    path("web/listar_comentarios/",ListarComentarios.as_view(), name="listar_comentarios"),


    path("web/crearComentario/",crearComentario.as_view(),name="dejar_comentario"),
    path("web/puntuacion/",Puntuacion.as_view(),name="puntuacion"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
