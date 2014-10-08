# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proyectojuego.apps.inicio.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=proyectojuego.apps.inicio.thumbs.ImageWithThumbsField(default=1, upload_to=b'img_user'),
            preserve_default=False,
        ),
    ]
