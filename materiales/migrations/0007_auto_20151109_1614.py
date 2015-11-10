# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_remove_curso_material'),
        ('materiales', '0006_material_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='curso',
        ),
        migrations.AddField(
            model_name='material',
            name='curso',
            field=models.ForeignKey(default=1, to='curso.Curso'),
            preserve_default=False,
        ),
    ]
