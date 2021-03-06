# Generated by Django 3.2 on 2021-05-17 14:19

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_capirca_plugin', '0010_auto_20210404_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acl',
            name='static_definitions_dir',
        ),
        migrations.AlterField(
            model_name='acl',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='acl',
            name='name',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='aclinterfaceassignment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
