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
            name='partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('jugadores', models.PositiveIntegerField()),
                ('tipo_partida', models.CharField(max_length=200, choices=[(b'public', b'Publico'), (b'private', b'Privado')])),
                ('preguntas', models.CharField(max_length=5, choices=[(b'10', b'10'), (b'20', b'20'), (b'30', b'30'), (b'40', b'40'), (b'50', b'50')])),
                ('tiempo_respuesta', models.CharField(max_length=5, choices=[(b'10', b'10'), (b'15', b'15'), (b'20', b'20'), (b'25', b'25'), (b'30', b'30'), (b'35', b'35'), (b'40', b'40'), (b'45', b'45'), (b'50', b'50'), (b'55', b'55'), (b'60', b'60')])),
                ('temas_sel', models.ManyToManyField(to='inicio.Tema')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
