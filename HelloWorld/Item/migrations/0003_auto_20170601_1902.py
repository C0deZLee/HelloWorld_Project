# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-01 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0002_auto_20170601_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
