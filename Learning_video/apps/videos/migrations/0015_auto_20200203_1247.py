# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-03 04:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20200201_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courese',
            name='liked',
        ),
        migrations.AlterField(
            model_name='courese',
            name='collected',
            field=models.ManyToManyField(blank=True, default=False, related_name='collected_videos', to=settings.AUTH_USER_MODEL, verbose_name='收藏'),
        ),
    ]
