# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-15 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20180815_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='live_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]