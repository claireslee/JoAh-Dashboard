# Generated by Django 4.1.5 on 2023-05-22 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djauth', '0011_auto_20230521_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='student',
            name='scores',
        ),
    ]
