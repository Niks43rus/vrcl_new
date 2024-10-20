# Generated by Django 3.2.19 on 2024-01-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_warninginfo_wi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_mg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=300, null=True)),
                ('after', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Молодой гвардии 51',
                'verbose_name_plural': 'Логи - Молодой гвардии 51',
            },
        ),
        migrations.CreateModel(
            name='Log_ms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=300, null=True)),
                ('after', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Московская 102в/1',
                'verbose_name_plural': 'Логи - Московская 102в/1',
            },
        ),
    ]
