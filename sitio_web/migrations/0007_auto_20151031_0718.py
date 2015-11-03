# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0006_auto_20151031_0159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cursos',
        ),
        migrations.DeleteModel(
            name='Proyectos',
        ),
    ]
