from django.db import models
from django.utils import timezone
# Create your models here.
 
class ModelsEstado(models.Model):
    estado = models.CharField(max_length=254, null = False)

class ModelsOcupacion (models.Model):
    ocupacion = models.CharField(max_length=254, null = False)

class ModelsGenero(models.Model):
    genero = models.CharField(max_length=254, null = False)

class ModelsCiudad(models.Model):
    ciudad = models.CharField(max_length=254, null = False)

class ModelsEstadoCivil(models.Model):
    estadocivil = models.CharField(max_length=254, null = False)


class Example3(models.Model):
    nombre = models.CharField(max_length=254, null = False)
    apPat = models.CharField(max_length=254, null = False)
    apMat = models.CharField(max_length=254, default = False)
    edad = models.IntegerField(null = False)

    estadocivil = models.ForeignKey(ModelsEstadoCivil,on_delete = models.CASCADE)
    ciudad = models.ForeignKey(ModelsCiudad,on_delete = models.CASCADE)
    ocupacion = models.ForeignKey(ModelsOcupacion,on_delete = models.CASCADE)
    estado= models.ForeignKey(ModelsEstado,on_delete = models.CASCADE)
    genero = models.ForeignKey(ModelsGenero,on_delete = models.CASCADE)

    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)
    def _str_(self):
        return self.nombre

    class Meta: 
        db_table = 'Example3'
  
    
