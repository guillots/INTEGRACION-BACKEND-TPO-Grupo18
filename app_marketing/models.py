from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre  = models.CharField(max_length=200)
    email  = models.CharField(max_length=200)
    servicio = models.CharField(max_length=200)
    valor = models.PositiveSmallIntegerField(blank=False,null=False)
    
class Meta:
    db_table = "usuarios_table"
    
