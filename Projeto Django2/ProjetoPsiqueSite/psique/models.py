from django.db import models

# Create your models here.
class Comentario(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    comentario = models.TextField('comentario')
    data = models.DateTimeField('data', auto_now_add=True)
    lido = models.BooleanField('Lido', default=False)

    def str(self):
            return f"{self.nome} - {self.data} - {self.lido}"