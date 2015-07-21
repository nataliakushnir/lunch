# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date_target',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='items',
            table='Item',
        ),
    ]
