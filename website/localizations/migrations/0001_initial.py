# Generated by Django 5.0.4 on 2024-04-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
                ('apartment_number', models.CharField(blank=True, max_length=10, null=True)),
                ('zip_code', models.CharField(max_length=10)),
                ('zip_code_city', models.CharField(max_length=100)),
                ('voivodeship', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adresy',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=100)),
                ('floor', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pomieszczenie',
                'verbose_name_plural': 'Pomieszczenia',
            },
        ),
    ]
