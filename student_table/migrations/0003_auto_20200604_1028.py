# Generated by Django 3.0.3 on 2020-06-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_table', '0002_auto_20200602_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]