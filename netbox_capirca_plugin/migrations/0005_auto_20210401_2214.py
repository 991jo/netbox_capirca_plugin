# Generated by Django 3.1.3 on 2021-04-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_capirca_plugin', '0004_auto_20210401_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='acl',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='acl',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
