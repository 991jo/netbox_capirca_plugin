# Generated by Django 3.1.3 on 2021-04-02 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0122_standardize_name_length'),
        ('netbox_capirca_plugin', '0006_auto_20210402_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACLInterfaceAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('direction', models.CharField(default='INGRESS', max_length=10)),
                ('acl', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='netbox_capirca_plugin.acl')),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcim.interface')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
