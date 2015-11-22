# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0015_evento_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='hora',
            field=models.DateField(default=datetime.datetime(2015, 11, 19, 0, 40, 43, 504089, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.TimeField(),
        ),
    ]
