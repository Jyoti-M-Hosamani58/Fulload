# Generated by Django 3.0 on 2024-12-14 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0017_auto_20241214_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullload',
            name='dedicationAmt',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fullload',
            name='dedicationReason',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='full_load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='consign_app.Fullload'),
        ),
    ]
