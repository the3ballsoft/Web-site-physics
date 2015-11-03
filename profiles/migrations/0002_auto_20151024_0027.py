# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AddField(
            model_name='user',
            name='is_docente',
            field=models.BooleanField(default=False),
        ),
    ]
