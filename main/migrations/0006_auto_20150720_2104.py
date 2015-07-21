# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150720_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_item',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_item',
            field=models.ManyToManyField(to='main.Items'),
        ),
    ]
