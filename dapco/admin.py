from django.contrib import admin

# Register your models here.
from .models import Encuesta, Pregunta, Opcion, Respuesta, Distribucion, Usuario
# Register your models here.


admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Respuesta)
admin.site.register(Distribucion)
admin.site.register(Usuario)