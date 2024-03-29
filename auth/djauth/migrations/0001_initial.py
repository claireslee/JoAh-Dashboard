# Generated by Django 4.1.7 on 2023-03-09 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    CLASS_CHOICES = (
        ('sat 230', 'SAT 230'),
        ('sat 450', 'SAT 450'),
        ('ap calc 33', 'AP CALC 33'),
        ('algebra 1 130', 'ALGEBRA 1 130'),
        ('act 689', 'ACT 689'),
    )

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checkLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('classes', models.CharField(max_length=20, choices=CLASS_CHOICES, default='sat 230')),
                ('questions', models.ManyToManyField('QuesModel', related_name='Exams')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=100)),
                ('classname', models.CharField(max_length=100)),
                ('gradelvl', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=100)),
                ('prefix', models.CharField(max_length=50)),
                ('classname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
