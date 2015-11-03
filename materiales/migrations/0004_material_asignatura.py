# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20151024_0152'),
        ('materiales', '0003_material_docente'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='asignatura',
            field=models.ForeignKey(default=1, to='curso.Curso'),
            preserve_default=False,
        ),
    ]
