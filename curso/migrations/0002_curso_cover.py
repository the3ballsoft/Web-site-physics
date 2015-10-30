# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='cover',
            field=models.ImageField(default=1, upload_to=b'cursos/', verbose_name=b'Asignaturas'),
            preserve_default=False,
        ),
    ]
