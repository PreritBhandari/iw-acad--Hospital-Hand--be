# Generated by Django 3.1 on 2020-08-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0008_auto_20200829_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
    ]
