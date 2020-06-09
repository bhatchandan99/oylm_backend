# Generated by Django 3.0.1 on 2020-06-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_table', '0013_auto_20200608_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='olympiad',
            name='name',
        ),
        migrations.RemoveField(
            model_name='olympiad',
            name='rupees',
        ),
        migrations.RemoveField(
            model_name='olympiad',
            name='subs',
        ),
        migrations.AddField(
            model_name='olympiad',
            name='cyberolym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='olympiad',
            name='englisholym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='olympiad',
            name='internationalspell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='olympiad',
            name='mathsolym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='olympiad',
            name='reasoningolym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='olympiad',
            name='scienceolym',
            field=models.BooleanField(default=False),
        ),
    ]
