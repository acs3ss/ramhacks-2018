# Generated by Django 2.1.1 on 2018-09-23 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20180922_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='videos',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
