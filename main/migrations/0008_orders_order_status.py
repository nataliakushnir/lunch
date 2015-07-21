# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150720_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_status',
            field=models.BooleanField(default=True),
        ),
    ]
