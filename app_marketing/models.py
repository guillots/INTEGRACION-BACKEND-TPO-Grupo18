from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre  = models.CharField(max_length=200)
    email  = models.CharField(max_length=200)
    
    
class Meta:
    db_table = "usuarios_table"
    

# def __str__(self):
#         return f"El vino: {self.nombre}, Rating {self.abv}"

# def get_fields(self):
#     return [
#         (field.verbose_name, field.value_from_object(self))
#         for field in self.__class__._meta.fields[1:]
#     ]

