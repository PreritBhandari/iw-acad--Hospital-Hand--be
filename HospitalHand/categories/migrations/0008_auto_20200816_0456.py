# Generated by Django 3.1 on 2020-08-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_auto_20200815_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ManyToManyField(to='categories.Department'),
        ),
    ]
