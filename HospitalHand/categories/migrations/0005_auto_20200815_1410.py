# Generated by Django 3.1 on 2020-08-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20200815_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='depart',
            field=models.CharField(max_length=100),
        ),
    ]
