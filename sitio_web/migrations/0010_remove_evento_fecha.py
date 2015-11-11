# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0009_remove_evento_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='fecha',
        ),
    ]
