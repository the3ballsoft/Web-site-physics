# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0014_frase_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 0, 27, 9, 764779, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
