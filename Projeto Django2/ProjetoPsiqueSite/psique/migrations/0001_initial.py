# Generated by Django 4.2.2 on 2023-06-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='nome')),
                ('comentario', models.TextField(verbose_name='comentario')),
                ('publicado', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('aprovado', models.BooleanField(default=False, verbose_name='aprovado')),
            ],
        ),
    ]