# Generated by Django 3.0 on 2024-12-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0002_transporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='fullload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_from', models.CharField(max_length=500, null=True)),
                ('route_to', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('vehicleNo', models.FloatField(max_length=500, null=True)),
                ('Tone', models.FloatField(null=True)),
                ('transport', models.CharField(max_length=500, null=True)),
                ('total', models.FloatField(null=True)),
                ('goods', models.CharField(max_length=500, null=True)),
                ('advance', models.FloatField(null=True)),
                ('balance', models.FloatField(null=True)),
                ('remark', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]