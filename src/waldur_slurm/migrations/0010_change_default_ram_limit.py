# Generated by Django 2.2.10 on 2020-05-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_slurm', '0009_introduce_allocation_user_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='ram_limit',
            field=models.BigIntegerField(default=102400000),
        ),
    ]
