# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:24
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0020_remove_matchreport_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentfullreport',
            name='new_sent',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentfullreport',
            name='new_to_address',
            field=models.TextField(
                null=True),
        ),
        migrations.AddField(
            model_name='sentmatchreport',
            name='new_sent',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentmatchreport',
            name='new_to_address',
            field=models.TextField(
                null=True),
        ),
    ]
