from django.db import models

class Pais(models.Model):
    
    def __str__(self):
        return self.nombre
    id = models.IntegerField( primary_key=True)
    nombre = models.CharField( max_length= 250)

class Departamento(models.Model):
    
    def __str__(self):
        return self.nombre
    
    id = models.IntegerField( primary_key=True)
    nombre = nombre = models.CharField( max_length= 250)
    pais = models.ForeignKey(Pais, verbose_name="Pais", on_delete=models.CASCADE)

class Ciudad(models.Model):
    
    def __str__(self):
        return self.nombre
    
    id = models.IntegerField( primary_key=True)
    nombre = nombre = models.CharField( max_length= 250)
    departamento = models.ForeignKey(Departamento, verbose_name="Departamento", on_delete=models.CASCADE)
