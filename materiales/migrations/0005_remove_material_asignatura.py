# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0004_material_asignatura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='asignatura',
        ),
    ]
