# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0010_material_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='tipo',
            field=models.CharField(default=b'taller', max_length=20, choices=[(b'quiz', b'Quiz'), (b'parcial', b'Parcial'), (b'taller', b'Taller'), (b'guia de laboratorio', b'Guia de Laboratorio'), (b'material de estudio', b'Material de estudio'), (b'lecturas', b'Lecturas')]),
        ),
    ]
