# Generated by Django 4.1.2 on 2022-10-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_sushi_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sushi',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]