# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-06 08:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0021_remove_allcoureslist_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('avatar', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Courese')),
            ],
            options={
                'db_table': 'v_comment',
            },
        ),
    ]
