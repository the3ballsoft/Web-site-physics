# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0013_frase'),
    ]

    operations = [
        migrations.AddField(
            model_name='frase',
            name='autor',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
