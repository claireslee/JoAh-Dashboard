# Generated by Django 4.1.7 on 2023-03-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(default='#', max_length=50)),
                ('topic', models.CharField(default='#', max_length=50)),
                ('announcement', models.CharField(max_length=100)),
            ],
        ),
    ]
