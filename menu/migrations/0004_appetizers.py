# Generated by Django 4.1.2 on 2022-10-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_sushi_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appetizers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
