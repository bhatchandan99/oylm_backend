# Generated by Django 3.0.3 on 2020-06-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_table', '0003_auto_20200604_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
