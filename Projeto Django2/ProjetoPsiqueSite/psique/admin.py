from django.contrib import admin
from .models import Comentario

# Register your models here.
class ComentAdmin(admin.ModelAdmin):
    list_display = ['nome', 'comentario', 'data']
    actions = ['validar_comentarios']

    def validar_comentarios(self, request, queryset):
        queryset.update(validado=True)

    validar_comentarios.short_description='Validar'
admin.site.register(Comentario, ComentAdmin)