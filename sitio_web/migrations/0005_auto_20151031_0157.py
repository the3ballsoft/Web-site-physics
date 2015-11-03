# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0004_auto_20151031_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='galeria',
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagenes',
            field=models.ForeignKey(default=1, to='sitio_web.Imagen'),
            preserve_default=False,
        ),
    ]
