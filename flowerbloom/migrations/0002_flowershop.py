# Generated by Django 3.2.23 on 2024-01-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerbloom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flowershop',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=255, verbose_name='Flower Name')),
            ],
        ),
    ]