from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuariosAdmin(admin.ModelAdmin):
    pass