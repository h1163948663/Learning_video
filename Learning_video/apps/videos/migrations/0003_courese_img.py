# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-21 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20190821_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='courese',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='图片描述'),
            preserve_default=False,
        ),
    ]
