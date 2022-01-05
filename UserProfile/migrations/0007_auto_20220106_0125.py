# Generated by Django 3.0.6 on 2022-01-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0006_userprofile_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile.png', upload_to='userProfile/profile_pic'),
        ),
    ]