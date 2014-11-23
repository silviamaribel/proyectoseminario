# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Juego_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_perdido', models.IntegerField()),
                ('part_ganado', models.IntegerField()),
                ('puntuacion', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo_p', models.CharField(max_length=150)),
                ('Tipo', models.CharField(max_length=15)),
                ('Num_preguntas', models.IntegerField()),
                ('categoria_par', models.ManyToManyField(to='inicio.Categorias')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo', models.CharField(max_length=150)),
                ('respuesta', models.CharField(max_length=150)),
                ('categoria', models.ManyToManyField(to='inicio.Categorias')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuestas_Opcionales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resp1', models.CharField(max_length=150)),
                ('resp3', models.CharField(max_length=150)),
                ('resp2', models.CharField(max_length=150)),
                ('pregunta', models.ForeignKey(to='inicio.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
