# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0008_auto_20151111_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material Academico', 'verbose_name_plural': 'Materiales Academicos '},
        ),
    ]
