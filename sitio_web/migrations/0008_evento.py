# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0007_auto_20151031_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, null=True, blank=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'eventos/', verbose_name=b'Evento')),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]
