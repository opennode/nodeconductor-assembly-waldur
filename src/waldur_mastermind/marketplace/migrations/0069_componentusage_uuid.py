# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-27 15:52
from __future__ import unicode_literals

from django.db import migrations
import waldur_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0068_componentusage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentusage',
            name='uuid',
            field=waldur_core.core.fields.UUIDField(),
        ),
    ]