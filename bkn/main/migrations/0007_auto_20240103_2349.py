# Generated by Django 3.2.19 on 2024-01-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_device_ms_note_ms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_ms',
            name='attendees_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество человек'),
        ),
        migrations.AlterField(
            model_name='note_ms',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя'),
        ),
        migrations.AlterField(
            model_name='note_ms',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='note_ms',
            name='time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='Время до'),
        ),
    ]
