# Generated by Django 4.1.2 on 2022-10-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_appetizers'),
    ]

    operations = [
        migrations.AddField(
            model_name='appetizers',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
