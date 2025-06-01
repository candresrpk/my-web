from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):\
    
    class Cargo(models.TextChoices):
        ENCUESTADOR = 'Encuestador', 'Encuestador'
        ADMINISTRADOR = 'Administrador', 'Administrador'
    
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='encuestadores')
    
    cargo = models.CharField(max_length=20,
                              choices=Cargo.choices,
                              default=Cargo.ENCUESTADOR
                            )
    
    
    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.user.username
    
    
class Encuesta(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='encuestas_usuarios')
    
    encuesta = models.CharField(max_length=200)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT
                              )

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __str__(self):
        return self.encuesta


class Distribucion(models.Model):
    encuestador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='encuestador_distribuciones')
    
    # DATOS DISTRIBUCION
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    barrio = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    comuna = models.CharField(max_length=200, blank=True, null=True)
    # TERMINAN ACA
    
    encuesta = models.ForeignKey(
        Encuesta, on_delete=models.CASCADE, related_name='encuesta_distribuciones')
    
    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Distribución'
        verbose_name_plural = 'Distribuciones'

    def __str__(self):
        return self.encuestador.user.username
    
    

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    encuesta = models.ForeignKey(
        Encuesta, on_delete=models.CASCADE, related_name='preguntas')

    def __str__(self):
        return self.pregunta


class Opcion(models.Model):

    class Categoria(models.TextChoices):
        MULTICHOICES = 'MC', 'Multichoice'
        OPEN = 'OP', 'Open'
        SINGLECHOICE = 'SC', 'Singlechoice'

    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.CASCADE, related_name='opciones')

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    opcion = models.CharField(max_length=200)
    categoria = models.CharField(
        max_length=200, choices=Categoria.choices, default=Categoria.SINGLECHOICE)

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'

    def __str__(self):
        return self.opcion


class Respuesta(models.Model):
    encuesta = models.ForeignKey(
        Encuesta, on_delete=models.PROTECT, related_name='encuestas')

    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.PROTECT, related_name='preguntas')

    opcion = models.ForeignKey(
        Opcion, on_delete=models.PROTECT, related_name='opciones')
    
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return f'{self.encuesta} - {self.pregunta} - {self.opcion.categoria}'