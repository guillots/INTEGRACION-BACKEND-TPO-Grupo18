from django.contrib import admin
from .models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    pass