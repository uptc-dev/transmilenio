# Generated by Django 2.1.2 on 2018-10-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0003_auto_20181003_0216'),
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='trunk',
            field=models.ManyToManyField(to='trunk.Trunk'),
        ),
    ]
