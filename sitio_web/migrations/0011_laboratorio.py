# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0010_remove_evento_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion')),
                ('titulo', models.CharField(max_length=255, null=True, blank=True)),
                ('informacion', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'laboratorios/', null=True, verbose_name=b'Laboratorios', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
