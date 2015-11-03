# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_curso_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.AlterField(
            model_name='curso',
            name='cover',
            field=models.ImageField(upload_to=b'cursos/', verbose_name=b'Imagen representativa'),
        ),
    ]
