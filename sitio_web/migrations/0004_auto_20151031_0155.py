# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0003_auto_20151015_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion')),
                ('imagen', models.ImageField(upload_to=b'galeria/', verbose_name=b'Galeria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='laboratorios',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='imagen',
        ),
        migrations.AddField(
            model_name='imagen',
            name='galeria',
            field=models.ForeignKey(to='sitio_web.Galeria'),
        ),
    ]
