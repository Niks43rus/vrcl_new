# Generated by Django 3.2.19 on 2024-01-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_settingssite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingssite',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
