# Generated by Django 3.2.16 on 2023-05-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djauth', '0008_test_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='questions',
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='test',
            field=models.ManyToManyField(related_name='questions', to='djauth.Test'),
        ),
    ]
