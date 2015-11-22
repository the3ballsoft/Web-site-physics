# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0017_auto_20151118_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora',
            field=models.TimeField(blank=True),
        ),
    ]
