# Generated by Django 3.0.1 on 2020-06-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_table', '0011_olympiad_rupees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='olympiad',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='olympiad',
            name='questions',
        ),
        migrations.AddField(
            model_name='olympiad',
            name='subs',
            field=models.BooleanField(default=False),
        ),
    ]