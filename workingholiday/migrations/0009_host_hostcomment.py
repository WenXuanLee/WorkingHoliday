# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingholiday', '0008_usercomment_commentarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='hostcomment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
