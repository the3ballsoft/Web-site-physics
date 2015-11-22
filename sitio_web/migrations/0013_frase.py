# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0012_auto_20151117_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frase', models.TextField()),
            ],
        ),
    ]
