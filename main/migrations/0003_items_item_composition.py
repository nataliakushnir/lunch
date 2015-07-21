# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150720_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_composition',
            field=models.TextField(max_length=200, blank=True),
        ),
    ]
