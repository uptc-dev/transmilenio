# Generated by Django 2.1.2 on 2018-10-03 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0002_auto_20181003_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trunk',
            old_name='start',
            new_name='first_letter',
        ),
    ]
