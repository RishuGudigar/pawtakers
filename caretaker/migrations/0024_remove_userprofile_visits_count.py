# Generated by Django 4.2 on 2023-06-18 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0023_rename_view_count_userprofile_visits_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='visits_count',
        ),
    ]
