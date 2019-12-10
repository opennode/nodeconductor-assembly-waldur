# Generated by Django 2.2.7 on 2019-12-09 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_project_is_removed'),
        ('waldur_rancher', '0006_node_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='tenant_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.ServiceSettings'),
        ),
    ]
