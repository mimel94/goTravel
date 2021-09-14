from django.db import models
from apps.paises.models import Ciudad
from apps.controlUsuarios.models import Usuario


class Ciudades(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField("Nombre", max_length=254)


class sitio(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField("Nombre", max_length=254)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    descripcion = models.CharField("Descripción", max_length=254 )
    album_url = models.ImageField("Foto",upload_to="sitios", null=True)
    ubicacion = models.CharField("Ubicacion", max_length=254, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)




