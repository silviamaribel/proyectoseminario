# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proyectojuego.apps.inicio.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_remove_perfil_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=proyectojuego.apps.inicio.thumbs.ImageWithThumbsField(upload_to=b'imagenusuario'),
        ),
    ]
