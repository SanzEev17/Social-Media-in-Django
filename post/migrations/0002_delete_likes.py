# Generated by Django 4.2.4 on 2023-09-01 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]