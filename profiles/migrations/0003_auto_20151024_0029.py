# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20151024_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_docente',
            new_name='es_docente',
        ),
    ]
