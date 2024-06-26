# Generated by Django 5.0.4 on 2024-05-06 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizations', '0004_alter_room_name'),
        ('users', '0002_customuser_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizations.room'),
        ),
    ]
