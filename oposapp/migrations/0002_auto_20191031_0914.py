# Generated by Django 2.2.2 on 2019-10-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oposapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='pin',
            field=models.IntegerField(max_length=4),
        ),
    ]
