from django.forms import ModelForm

from .models import Comentario

class ComentForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'comentario']