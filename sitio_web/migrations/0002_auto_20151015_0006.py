# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='imagen',
            field=models.ImageField(default=3, upload_to=b'noticias/', verbose_name=b'Noticias'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docentes',
            name='imagen',
            field=models.ImageField(upload_to=b'docentes/', null=True, verbose_name=b'Galeria', blank=True),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'fecha de actualizacion'),
        ),
    ]
