# Generated by Django 3.2.5 on 2021-08-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(auto_now_add=True),
        ),
    ]
