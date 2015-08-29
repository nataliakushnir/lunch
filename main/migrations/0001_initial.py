# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('count', models.PositiveSmallIntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('weight', models.FloatField(max_length=6)),
                ('price', models.FloatField(max_length=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='main.Category')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='main.Dish', through='main.Calculate')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='calendar',
            name='dish',
            field=models.ForeignKey(to='main.Dish'),
        ),
        migrations.AddField(
            model_name='calculate',
            name='dish',
            field=models.ForeignKey(to='main.Dish'),
        ),
        migrations.AddField(
            model_name='calculate',
            name='order',
            field=models.ForeignKey(to='main.Order'),
        ),
    ]
