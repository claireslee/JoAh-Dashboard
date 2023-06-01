# Generated by Django 4.1.7 on 2023-06-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djauth', '0017_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='#', max_length=50)),
                ('email', models.EmailField(default='#', max_length=200)),
                ('subject', models.CharField(default='#', max_length=50)),
                ('message', models.CharField(default='#', max_length=500)),
            ],
        ),
    ]
