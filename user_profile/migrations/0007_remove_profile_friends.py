# Generated by Django 4.2.4 on 2023-08-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_profile_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]
