# Generated by Django 4.2.4 on 2023-09-04 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_profile_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
    ]
