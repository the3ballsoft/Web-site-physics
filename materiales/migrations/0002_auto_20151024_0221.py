# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='material',
        ),
        migrations.AddField(
            model_name='material',
            name='arichivo',
            field=models.FileField(default=1, upload_to=b'materiales/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Archivo',
        ),
    ]
