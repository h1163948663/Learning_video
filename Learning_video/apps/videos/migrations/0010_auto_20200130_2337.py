# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-30 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20200130_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courese',
            name='courese_name',
            field=models.CharField(max_length=128, verbose_name='课程名称'),
        ),
    ]
