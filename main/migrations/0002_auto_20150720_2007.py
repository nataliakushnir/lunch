# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dishes',
            table='Dishes',
        ),
        migrations.AlterModelTable(
            name='items',
            table='Items',
        ),
    ]
