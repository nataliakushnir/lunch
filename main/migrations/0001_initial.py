# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish_description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.TextField(max_length=200)),
                ('item_weight', models.CommaSeparatedIntegerField(max_length=20)),
                ('item_price', models.FloatField(max_length=20)),
                ('item_status', models.BooleanField(default=False)),
                ('item_date_add', models.DateTimeField(auto_now_add=True)),
                ('item_description', models.ForeignKey(to='main.Dishes')),
            ],
        ),
    ]
