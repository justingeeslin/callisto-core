# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0020_choiceoption_typo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='multiple',
        ),
        migrations.RemoveField(
            model_name='page',
            name='name_for_multiple',
        ),
    ]
