# Generated by Django 4.2.4 on 2023-10-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'STAFF'), (3, 'STUDENT'), (4, 'BRANCH'), (5, 'ACCOUNTANT'), (6, 'DEVELOPER')], default=1, max_length=50),
        ),
    ]
