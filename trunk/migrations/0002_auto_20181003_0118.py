# Generated by Django 2.1.2 on 2018-10-03 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trunk',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='trunk',
            name='end',
        ),
    ]
