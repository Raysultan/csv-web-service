# Generated by Django 3.0.2 on 2020-01-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200125_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gems',
            field=models.ManyToManyField(blank=True, related_name='clients', to='core.Item'),
        ),
    ]
