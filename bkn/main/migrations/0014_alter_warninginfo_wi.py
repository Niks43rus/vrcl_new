# Generated by Django 3.2.19 on 2024-01-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_warninginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warninginfo',
            name='WI',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Информация'),
        ),
    ]