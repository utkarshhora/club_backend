# Generated by Django 3.0.7 on 2020-06-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_userprofile_is_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
