from django.db import models

# Create your models here.

class Persona(models.Model):
    # Atributos vacios
    nombre = None
    apellido = None
    edad = None
    dni = None
    email = None
    direccion = None
    telefono = None
    fecha_nacimiento = None



    # Metodo constructo



    class Meta:
        abstract = True
