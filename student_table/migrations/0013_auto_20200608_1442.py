# Generated by Django 3.0.1 on 2020-06-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_table', '0012_auto_20200608_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olympiad',
            name='rupees',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='subs',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
