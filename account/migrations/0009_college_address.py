# Generated by Django 4.2.4 on 2023-11-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_grouptime_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
