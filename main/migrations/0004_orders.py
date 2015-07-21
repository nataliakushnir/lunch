# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_items_item_composition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date_published', models.DateTimeField(auto_now_add=True)),
                ('order_date_target', models.DateTimeField()),
                ('order_item', models.ForeignKey(to='main.Items')),
            ],
        ),
    ]
