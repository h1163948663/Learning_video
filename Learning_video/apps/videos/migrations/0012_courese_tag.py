# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-23 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_auto_20190824_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='courese',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.Category', verbose_name='标签'),
        ),
    ]
