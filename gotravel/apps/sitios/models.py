from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from apps.paises.models import Ciudad
from apps.controlUsuarios.models import Usuario


class Ciudades(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField("Nombre", max_length=254)


class sitio(models.Model):
    def __str__(self):
        return self.nombre

    TIPO_SITIOS = (
        ("finca","Finca"),
        ("centro_recreacional","Centro Recreacional"),
        ("parque","Parque")
    )

    nombre = models.CharField("Nombre", max_length=254)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    descripcion = models.CharField("Descripción", max_length=254 )
    tipo = models.CharField("tipo", max_length=100, choices=TIPO_SITIOS,default="nn")
    album_url = models.ImageField("Foto",upload_to="sitios", null=True)
    ubicacion = models.CharField("Ubicacion", max_length=254, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentarios(models.Model):

    def __str__(self):
        return self.comentario

    comentario = models.CharField("Comentario", max_length=254)
    sitio = ForeignKey(sitio,  on_delete=models.CASCADE)
    usuario = ForeignKey(Usuario,  on_delete=models.CASCADE)

class Puntuacion (models.Model):
    
    def __str__(self):
        return str(self.Puntuacion)

    Puntuacion = models.IntegerField()
    sitio = ForeignKey(sitio,  on_delete=models.CASCADE)
    usuario = ForeignKey(Usuario,  on_delete=models.CASCADE)


