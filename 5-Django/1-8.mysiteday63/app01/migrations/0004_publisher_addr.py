# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180503_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='addr',
            field=models.CharField(default='丰善东路', max_length=128),
            preserve_default=False,
        ),
    ]
