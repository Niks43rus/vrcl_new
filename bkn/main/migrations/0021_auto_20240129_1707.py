# Generated by Django 3.2.19 on 2024-01-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20240125_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device_arle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - АРЕНА Ленина 95а',
            },
        ),
        migrations.CreateModel(
            name='Device_arur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - АРЕНА Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='Device_iz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - Ижевск - Ленина 18',
            },
        ),
        migrations.CreateModel(
            name='Device_kl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - Калинина 40',
            },
        ),
        migrations.CreateModel(
            name='Device_le',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - Ленина 91',
            },
        ),
        migrations.CreateModel(
            name='Device_ur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name_plural': 'Устройства - Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='graph_arle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - АРЕНА Ленина 95а',
                'verbose_name_plural': 'График смен - АРЕНА Ленина 95а',
            },
        ),
        migrations.CreateModel(
            name='graph_arur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - АРЕНА Уральская 1',
                'verbose_name_plural': 'График смен - АРЕНА Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='graph_iz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - Ижевск - Ленина 18',
                'verbose_name_plural': 'График смен - Ижевск - Ленина 18',
            },
        ),
        migrations.CreateModel(
            name='graph_kl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - Калинина 40',
                'verbose_name_plural': 'График смен - Калинина 40',
            },
        ),
        migrations.CreateModel(
            name='graph_le',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - Ленина 91',
                'verbose_name_plural': 'График смен - Ленина 91',
            },
        ),
        migrations.CreateModel(
            name='graph_ur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('Admin_one', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_two', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_three', models.CharField(blank=True, max_length=60, null=True)),
                ('Admin_four', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'График смен  - Уральская 1',
                'verbose_name_plural': 'График смен - Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='Log_arle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - АРЕНА Ленина 95а',
                'verbose_name_plural': 'Логи - АРЕНА Ленина 95а',
            },
        ),
        migrations.CreateModel(
            name='Log_arur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - АРЕНА Уральская 1',
                'verbose_name_plural': 'Логи - АРЕНА Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='Log_iz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Ижевск - Ленина 18',
                'verbose_name_plural': 'Логи - Ижевск - Ленина 18',
            },
        ),
        migrations.CreateModel(
            name='Log_kl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Калинина 40',
                'verbose_name_plural': 'Логи - Калинина 40',
            },
        ),
        migrations.CreateModel(
            name='Log_le',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Ленина 91',
                'verbose_name_plural': 'Логи - Ленина 91',
            },
        ),
        migrations.CreateModel(
            name='Log_ur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('who', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('before', models.CharField(max_length=600, null=True)),
                ('after', models.CharField(max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'Логи - Уральская 1',
                'verbose_name_plural': 'Логи - Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='Note_arle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Киров - АРЕНА Ленина 95а',
            },
        ),
        migrations.CreateModel(
            name='Note_arur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Киров - АРЕНА Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='Note_iz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Ижевск - Ленина 18',
            },
        ),
        migrations.CreateModel(
            name='Note_kl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Киров - Калинина 40',
            },
        ),
        migrations.CreateModel(
            name='Note_le',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Киров - Ленина 91',
            },
        ),
        migrations.CreateModel(
            name='Note_ur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time_from', models.TimeField(verbose_name='Время с')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Время до')),
                ('devices', models.CharField(blank=True, max_length=500, verbose_name='Устройства')),
                ('attendees_count', models.CharField(blank=True, max_length=60, null=True, verbose_name='Количество человек')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия и имя')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('where', models.CharField(blank=True, max_length=50, null=True, verbose_name='Откуда')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кем сделана')),
            ],
            options={
                'verbose_name_plural': 'Записи Киров - Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='place_arle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - АРЕНА Ленина 95а',
                'verbose_name_plural': 'Места - АРЕНА Ленина 95а',
            },
        ),
        migrations.CreateModel(
            name='place_arur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - АРЕНА Уральская 1',
                'verbose_name_plural': 'Места - АРЕНА Уральская 1',
            },
        ),
        migrations.CreateModel(
            name='place_iz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - Ижевск - Ленина 18',
                'verbose_name_plural': 'Места - Ижевск - Ленина 18',
            },
        ),
        migrations.CreateModel(
            name='place_kl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - Калинина 40',
                'verbose_name_plural': 'Места - Калинина 40',
            },
        ),
        migrations.CreateModel(
            name='place_le',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - Ленина 91',
                'verbose_name_plural': 'Места - Ленина 91',
            },
        ),
        migrations.CreateModel(
            name='place_ur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Места - Уральская 1',
                'verbose_name_plural': 'Места - Уральская 1',
            },
        ),
        migrations.AlterModelOptions(
            name='admins',
            options={'verbose_name_plural': 'Настройки - Админы'},
        ),
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name_plural': 'Настройки - Клубы'},
        ),
        migrations.AlterModelOptions(
            name='settingssite',
            options={'verbose_name_plural': 'Настройки - Общие'},
        ),
    ]