# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0005_auto_20151031_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagenes',
            field=models.ManyToManyField(to='sitio_web.Imagen'),
        ),
    ]
