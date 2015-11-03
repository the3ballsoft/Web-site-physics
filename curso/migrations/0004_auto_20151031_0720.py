# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20151024_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='descripcion',
        ),
    ]
