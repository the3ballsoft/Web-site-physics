# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0011_laboratorio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docentes',
            options={'verbose_name': 'Planta Docente', 'verbose_name_plural': 'Planta Docente'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name': 'Programar Evento', 'verbose_name_plural': 'Programacion de Eventos'},
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'verbose_name': 'Galeria de Imagenes', 'verbose_name_plural': 'Galerias de Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='noticias',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterModelOptions(
            name='presentacion',
            options={'verbose_name': 'Presentacion del Area', 'verbose_name_plural': 'Presentacion del Area'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Red Social', 'verbose_name_plural': 'Redes Sociales'},
        ),
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'verbose_name': 'Ubicacion de la Universidad', 'verbose_name_plural': 'Ubicacion de la Universidad'},
        ),
    ]
