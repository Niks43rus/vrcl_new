# main/models.py
from django.db import models


# Клубы
class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Настройки - Клубы'


# Настройки сайта
class SettingsSite(models.Model):
    name = models.CharField(max_length=1000, unique=True)  # сделаем поле name уникальным
    keys = models.TextField(max_length=4000)

    def __str__(self):
        return self.name + ": " + self.keys

    class Meta:
        verbose_name_plural = 'Настройки - Общие'

    # функция для получения ключа по имени
    @classmethod
    def get_password_by_name(cls, name):
        try:
            return cls.objects.get(name=name).keys
        except cls.DoesNotExist:
            return None


#Админы
class Admins(models.Model):
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Настройки - Админы'


#Важная информация
class WarningInfo(models.Model):
    ClubName = models.CharField(max_length=50, verbose_name='Имя клуба')
    WI = models.CharField(max_length=50, verbose_name='Информация', blank=True, null=True)

    def __str__(self):
        return f'{self.ClubName} {self.WI}'

    class Meta:
        verbose_name_plural = 'Важная информация'


#Статистика откуда
class WhereInfo(models.Model):
    where = models.CharField(max_length=50, verbose_name='Откуда')
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.where} {self.counter}'

    class Meta:
        verbose_name_plural = 'Статистика - Откуда'


#Набор игр
class Games_for_place(models.Model):
    Name = models.CharField(max_length=250, verbose_name='Название')
    Alt_name = models.CharField(max_length=250, verbose_name='Альтернативное название')


    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name_plural = 'Стек игр'


class GamePlace(models.Model):
    game = models.ForeignKey(Games_for_place, on_delete=models.CASCADE, related_name="game_places", verbose_name="Игра")
    place = models.CharField(max_length=100, verbose_name="Место")
    club = models.CharField(max_length=250, verbose_name="Клуб")

    def __str__(self):
        return f"{self.game.Name} - {self.place} ({self.club})"

    class Meta:
        verbose_name = "Привязка игры к месту"
        verbose_name_plural = "Привязки игр к местам"



class News(models.Model):
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")  # Используем TextField для длинных текстов
    date = models.DateTimeField(verbose_name="Дата публикации")  # Поле для даты
    source = models.CharField(max_length=250, verbose_name="Автор")  # Поле для источника новости

    def __str__(self):
        return f"{self.title} ({self.source}, {self.date.strftime('%Y-%m-%d')})"
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"




#region Молодой гвардии
class Device_mg(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Молодой гвардии 51'

class Note_mg(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - Молодой гвардии 51'

class Log_mg(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Молодой гвардии 51"
        verbose_name = "Логи - Молодой гвардии 51"

class place_mg(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Молодой гвардии 51"
        verbose_name = "Места - Молодой гвардии 51"

class graph_mg(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Молодой гвардии 51"
        verbose_name = "График смен  - Молодой гвардии 51"
#endregion


#region Московская
class Device_ms(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Московская 102в/1'

class Note_ms(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - Московская 102в/1'

class Log_ms(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Московская 102в/1"
        verbose_name = "Логи - Московская 102в/1"

class place_ms(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Московская 102в/1"
        verbose_name = "Места - Московская 102в/1"


class graph_ms(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Московская 102в/1"
        verbose_name = "График смен  - Московская 102в/1"
#endregion


#region Киров - Ленина 91
class Device_le(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Ленина 91'

class Note_le(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - Ленина 91'

class Log_le(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Ленина 91"
        verbose_name = "Логи - Ленина 91"

class place_le(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Ленина 91"
        verbose_name = "Места - Ленина 91"


class graph_le(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Ленина 91"
        verbose_name = "График смен  - Ленина 91"
#endregion


#region Киров - Калинина 40
class Device_kl(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Калинина 40'

class Note_kl(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - Калинина 40'

class Log_kl(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Калинина 40"
        verbose_name = "Логи - Калинина 40"

class place_kl(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Калинина 40"
        verbose_name = "Места - Калинина 40"

class graph_kl(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Калинина 40"
        verbose_name = "График смен  - Калинина 40"

#endregion


#region Киров - АРЕНА Ленина 95а
class Device_arle(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - АРЕНА Ленина 95а'

class Note_arle(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - АРЕНА Ленина 95а'

class Log_arle(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - АРЕНА Ленина 95а"
        verbose_name = "Логи - АРЕНА Ленина 95а"

class place_arle(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - АРЕНА Ленина 95а"
        verbose_name = "Места - АРЕНА Ленина 95а"

class graph_arle(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - АРЕНА Ленина 95а"
        verbose_name = "График смен  - АРЕНА Ленина 95а"

#endregion


#region Киров - АРЕНА Уральская 1
class Device_arur(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - АРЕНА Уральская 1'

class Note_arur(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - АРЕНА Уральская 1'

class Log_arur(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - АРЕНА Уральская 1"
        verbose_name = "Логи - АРЕНА Уральская 1"

class place_arur(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - АРЕНА Уральская 1"
        verbose_name = "Места - АРЕНА Уральская 1"

class graph_arur(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - АРЕНА Уральская 1"
        verbose_name = "График смен  - АРЕНА Уральская 1"

#endregion


#region Киров - Уральская 1
class Device_ur(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Уральская 1'

class Note_ur(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Киров - Уральская 1'

class Log_ur(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Уральская 1"
        verbose_name = "Логи - Уральская 1"

class place_ur(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Уральская 1"
        verbose_name = "Места - Уральская 1"

class graph_ur(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Уральская 1"
        verbose_name = "График смен  - Уральская 1"

#endregion


#region Ижевск - Ленина 18
class Device_iz(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Устройства - Ижевск - Ленина 18'

class Note_iz(models.Model):
    date = models.DateField(verbose_name='Дата')
    time_from = models.TimeField(verbose_name='Время с')
    time_to = models.TimeField(verbose_name='Время до', blank=True, null=True)
    devices = models.CharField(max_length=500, verbose_name='Устройства', blank=True)
    attendees_count = models.CharField(max_length=60, verbose_name='Количество человек', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия и имя', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    additional_info = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    where = models.CharField(max_length=50, verbose_name='Откуда', blank=True, null=True)
    who = models.CharField(max_length=50, verbose_name='Кем сделана', blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.time_from}-{self.time_to} {self.devices} {self.attendees_count} {self.full_name} {self.phone_number} {self.additional_info} {self.where} {self.who}'

    class Meta:
        verbose_name_plural = 'Записи Ижевск - Ленина 18'

class Log_iz(models.Model):
    when = models.DateTimeField()
    who = models.CharField(null=True, max_length=50)
    operation = models.CharField(null=True, max_length=50)
    before = models.CharField(null=True, max_length=600)
    after = models.CharField(null=True, max_length=600)


    def __str__(self):
        return f'{self.when} + {self.operation} + {self.before} + {self.after}'

    class Meta:
        verbose_name_plural = "Логи - Ижевск - Ленина 18"
        verbose_name = "Логи - Ижевск - Ленина 18"

class place_iz(models.Model):
    place = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name_plural = "Места - Ижевск - Ленина 18"
        verbose_name = "Места - Ижевск - Ленина 18"

class graph_iz(models.Model):
    date = models.DateTimeField(blank=True)
    Admin_one = models.CharField(null=True, blank=True, max_length=60)
    Admin_two = models.CharField(null=True, blank=True, max_length=60)
    Admin_three = models.CharField(null=True,blank=True, max_length=60)
    Admin_four = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return f'{self.date} {self.Admin_one} {self.Admin_two} {self.Admin_three} {self.Admin_four}'

    class Meta:
        verbose_name_plural = "График смен - Ижевск - Ленина 18"
        verbose_name = "График смен  - Ижевск - Ленина 18"

#endregion
