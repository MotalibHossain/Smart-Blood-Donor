# Generated by Django 3.0.6 on 2022-01-03 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0002_auto_20211205_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodrequestpost',
            options={'ordering': ['-currentDate']},
        ),
    ]
