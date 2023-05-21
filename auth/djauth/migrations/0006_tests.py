
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('djauth', '0001_initial'),
    ]
 
    CLASS_CHOICES = (
        ('sat 230', 'SAT 230'),
        ('sat 450', 'SAT 450'),
        ('ap calc 33', 'AP CALC 33'),
        ('algebra 1 130', 'ALGEBRA 1 130'),
        ('act 689', 'ACT 689'),
    )

    operations = [
        migrations.CreateModel(
                    name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('classes', models.CharField(max_length=20, choices=CLASS_CHOICES, default='sat 230')),
                ('questions', models.ManyToManyField('QuesModel', related_name='Exams')),
            ],
        ),
    ]