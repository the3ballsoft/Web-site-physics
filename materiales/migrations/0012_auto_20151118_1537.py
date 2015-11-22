# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0011_auto_20151117_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
