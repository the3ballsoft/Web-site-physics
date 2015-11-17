# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_remove_curso_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Asignatura', 'verbose_name_plural': 'Asignaturas'},
        ),
    ]
