# Generated by Django 4.2.4 on 2023-11-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouptime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]