# Generated by Django 3.0 on 2020-02-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursionapp', '0006_auto_20200214_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='minimumAge',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
