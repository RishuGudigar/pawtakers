# Generated by Django 4.2 on 2023-05-22 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0012_userprofile_tion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tion',
        ),
    ]