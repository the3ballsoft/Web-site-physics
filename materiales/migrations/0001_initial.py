# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion')),
                ('arichivo', models.FileField(upload_to=b'materiales/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('material', models.ManyToManyField(to='materiales.Archivo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
