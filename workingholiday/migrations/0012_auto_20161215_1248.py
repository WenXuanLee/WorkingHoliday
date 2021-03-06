# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingholiday', '0011_auto_20161215_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymanage',
            name='applyEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='applymanage',
            name='applyhostemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='confirmmanage',
            name='confirmEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='confirmusermanage',
            name='confirmHostEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
