# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-13 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingholiday', '0004_auto_20161213_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='hostpicture',
            field=models.URLField(blank=True, null=True),
        ),
    ]