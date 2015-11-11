# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0007_auto_20151109_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='arichivo',
            field=models.FileField(null=True, upload_to=b'materiales/', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
