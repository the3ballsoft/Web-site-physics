# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='es_docente',
            field=models.BooleanField(default=True),
        ),
    ]
