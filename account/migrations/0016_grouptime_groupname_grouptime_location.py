# Generated by Django 4.2.4 on 2023-12-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_remove_branch_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptime',
            name='groupname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grouptime',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
