# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0005_remove_material_asignatura'),
        ('curso', '0004_auto_20151031_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='material',
            field=models.ManyToManyField(to='materiales.Material'),
        ),
    ]
