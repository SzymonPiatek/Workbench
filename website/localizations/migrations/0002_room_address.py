# Generated by Django 5.0.4 on 2024-05-05 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='localizations.address'),
        ),
    ]
