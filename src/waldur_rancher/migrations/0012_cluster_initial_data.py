# Generated by Django 2.2.9 on 2020-02-19 14:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_rancher', '0011_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='initial_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                help_text='Initial data for instance creating.',
            ),
        ),
    ]
