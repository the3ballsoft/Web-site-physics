# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_remove_curso_material'),
        ('materiales', '0005_remove_material_asignatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='curso',
            field=models.ManyToManyField(to='curso.Curso'),
        ),
    ]
