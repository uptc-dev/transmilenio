# Generated by Django 2.1.2 on 2018-10-05 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trunk', '0001_initial'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station', to='stations.Station')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_accessor', to='transfers.Transfer')),
                ('trunk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trunk', to='trunk.Trunk')),
            ],
        ),
    ]
