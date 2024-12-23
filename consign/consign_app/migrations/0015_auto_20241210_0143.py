# Generated by Django 3.0 on 2024-12-09 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0014_auto_20241210_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullloadexpenses',
            name='branch',
        ),
        migrations.AlterField(
            model_name='balance',
            name='full_load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='consign_app.Fullload'),
        ),
    ]