# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180223_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='initial_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_price',
            field=models.FloatField(default=0.0),
        ),
    ]