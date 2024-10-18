# main/views.py
import json
import re
import random
from django.shortcuts import render, redirect
from datetime import datetime, timedelta, date
from .models import *
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import F, ExpressionWrapper, DateTimeField, Case, When, Value
from django.db import connections

club_models_notes = {
    'Киров - Молодой Гвардии 51': Note_mg,
    'Киров - Московская 102в/1': Note_ms,
    'Киров - Ленина 91': Note_le,
    'Киров - Калинина 40': Note_kl,
    'Киров - АРЕНА Ленина 95а': Note_arle,
    'Киров - АРЕНА Уральская 1': Note_arur,
    'Киров - Уральская 1': Note_ur,
    'Ижевск - Ленина 18': Note_iz,
}

club_models_devices = {
    'Киров - Молодой Гвардии 51': Device_mg,
    'Киров - Московская 102в/1': Device_ms,
    'Киров - Ленина 91': Device_le,
    'Киров - Калинина 40': Device_kl,
    'Киров - АРЕНА Ленина 95а': Device_arle,
    'Киров - АРЕНА Уральская 1': Device_arur,
    'Киров - Уральская 1': Device_ur,
    'Ижевск - Ленина 18': Device_iz,
}

club_models_log = {
    'Киров - Молодой Гвардии 51': Log_mg,
    'Киров - Московская 102в/1': Log_ms,
    'Киров - Ленина 91': Log_le,
    'Киров - Калинина 40': Log_kl,
    'Киров - АРЕНА Ленина 95а': Log_arle,
    'Киров - АРЕНА Уральская 1': Log_arur,
    'Киров - Уральская 1': Log_ur,
    'Ижевск - Ленина 18': Log_iz,
}

club_models_places = {
    'Киров - Молодой Гвардии 51': place_mg,
    'Киров - Московская 102в/1': place_ms,
    'Киров - Ленина 91': place_le,
    'Киров - Калинина 40': place_kl,
    'Киров - АРЕНА Ленина 95а': place_arle,
    'Киров - АРЕНА Уральская 1': place_arur,
    'Киров - Уральская 1': place_ur,
    'Ижевск - Ленина 18': place_iz,
}

club_models_graph = {
    'Киров - Молодой Гвардии 51': graph_mg,
    'Киров - Московская 102в/1': graph_ms,
    'Киров - Ленина 91': graph_le,
    'Киров - Калинина 40': graph_kl,
    'Киров - АРЕНА Ленина 95а': graph_arle,
    'Киров - АРЕНА Уральская 1': graph_arur,
    'Киров - Уральская 1': graph_ur,
    'Ижевск - Ленина 18': graph_iz,
}


# Главная страница
def index(request):
    clubs = Club.objects.all()
    expected_password = SettingsSite.get_password_by_name("Пароль для входа")
    return render(request, 'main/index.html', {'clubs': clubs, 'expected_password': expected_password})


# Функция для проверки авторизации пользователя
def is_authenticated(request):
    authenticated_password = request.COOKIES.get("authenticated")
    expected_password = SettingsSite.get_password_by_name("Пароль для входа")
    return authenticated_password == expected_password


from urllib.parse import unquote


# Страница клуба
def club_page(request):
    cl_E = request.COOKIES.get("clubName")
    cl = unquote(cl_E) if cl_E else None

    # Проверяем авторизацию пользователя
    if is_authenticated(request):
        clubs = Club.objects.all()
        admins = Admins.objects.all().order_by('name')
        devices_model = club_models_devices.get(str(cl))
        action_and_part = SettingsSite.get_password_by_name("Акции и партнеры")

        # devices = devices_model.objects.all().order_by('name')

        if devices_model:
            devices = devices_model.objects.all().order_by('name')
        else:
            devices = None

        place_model = club_models_places.get(str(cl))
        places = place_model.objects.all().order_by('place')

        wi_model = WarningInfo.objects.get(ClubName=cl)

        club = Club.objects.get(name=cl)
        club_id = club.id

        context = {
            'club_name': cl,
            'CID': club_id,
            'admins': admins,
            'clubs': clubs,
            'WI': wi_model.WI,
            'devices': devices,
            'places': places,
            'action_and_part': action_and_part,
        }

        return render(request, 'main/club_page.html', context)

    return redirect('index')


def get_notes_data(request, club_id):
    club_name = Club.objects.get(id=int(club_id))
    notes_model = club_models_notes.get(str(club_name))

    # Аннотация, чтобы добавить поле для сравнения с полуночью
    notes_data = notes_model.objects.annotate(
        adjusted_time_from=ExpressionWrapper(
            F('time_from') + Case(
                When(time_from__lt='08:00', then=Value(timedelta(days=1))),
                default=Value(timedelta(0)),
                output_field=DateTimeField(),
            ),
            output_field=DateTimeField(),
        )
    ).order_by('date', 'adjusted_time_from').values()

    notes_data_list = list(notes_data)

    return JsonResponse({'notes_data': notes_data_list})



# Получение строки гостя из базы гостей для нажатия по номеру
def get_phone_number_data(request):
    # Extract phone number from the GET parameters
    phone_number = request.GET.get('phoneNumber', None)
    print(phone_number)

    if phone_number:
        cleaned_phone_number = ''.join(char for char in phone_number if char.isdigit())
        print(cleaned_phone_number)

        with connections['guest_tab'].cursor() as cursor:
            query = "SELECT * FROM main_guest_tab WHERE guest_phone = %s"
            cursor.execute(query, [cleaned_phone_number])
            guest_tab_data = cursor.fetchone()
            print(guest_tab_data)

        return JsonResponse({'status': 'success', 'guest_tab_data': guest_tab_data})
    else:
        # Return an error response if phoneNumber parameter is not provided
        return JsonResponse({'status': 'error', 'message': 'phoneNumber parameter is required'}, status=400)


# изменение важной информации
def save_warning_info(request):
    if request.method == 'POST':
        # region Получаем данные из запроса
        club_name = request.POST.get('clubName')
        new_info = request.POST.get('newText')
        # endregion

        try:
            # Получаем объект WarningInfo по имени клуба
            wi_model = WarningInfo.objects.get(ClubName=club_name)
            # Обновляем информацию
            wi_model.WI = new_info
            # Сохраняем изменения
            wi_model.save()
        except WarningInfo.DoesNotExist:
            # Если объект не найден, создаем новый
            WarningInfo.objects.create(ClubName=club_name, WI=new_info)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


# Добавление записи
def save_record(request):
    if request.method == 'POST':
        # region Получаем данные из запроса
        club_id = request.POST.get('clubId')
        date = request.POST.get('date')
        time_from = request.POST.get('time_from')
        time_to = request.POST.get('time_to')
        devices = request.POST.get('devices')
        attendees_count = request.POST.get('attendees_count')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        additional_info = request.POST.get('additional_info')
        rent_checkbox = request.POST.get('rent_checkbox') == 'true'

        where = request.POST.get('where_select')
        who = request.POST.get('activeAdmin')
        club_name = request.POST.get('clubName')

        # получение модели по имени клуба
        notes_model = club_models_notes.get(club_name)
        # endregion

        # region проверки / исправления в нужный формат для таблицы

        if full_name == "":
            full_name = "БЕЗ ИМЕНИ"

        if phone_number == "":
            phone_number = "БЕЗ НОМЕРА"

        if attendees_count == "":
            attendees_count = "-"

        # Проверка / правка наличия даты
        if not date:
            return HttpResponseBadRequest('Не корректная дата')

        # Проверка наличия даты, времени с, времени до и выбранных устройств
        if not time_from:
            return HttpResponseBadRequest('Нет времени с')

        # Проверка наличия времени окончания
        if not time_to:
            # Если время окончания не указано, устанавливаем его как время начала + 3 часа
            time_to = (datetime.strptime(time_from, '%H:%M') + timedelta(hours=3)).strftime('%H:%M')

        # Парсим время начала и окончания
        time_from_dt = datetime.strptime(time_from, '%H:%M')
        time_to_dt = datetime.strptime(time_to, '%H:%M')

        # Проверка корректности времени
        if time_to_dt < time_from_dt:
            # Время окончания на следующий день, увеличиваем дату окончания на 1 день
            time_to_dt += timedelta(days=1)

        # Проверка корректности времени (теперь time_to_dt всегда больше time_from_dt)
        if time_to_dt <= time_from_dt:
            print("Время окончания не может быть раньше времени начала")
            return HttpResponseBadRequest('Время окончания не может быть раньше времени начала')

        # Проверка на ночное время (если нужно)
        night_start = datetime.strptime("23:00", '%H:%M')
        night_end = datetime.strptime("01:00", '%H:%M')

        if night_start <= time_from_dt <= night_end or night_start <= time_to_dt <= night_end:
            print("Запись в ночное время не разрешена")
            return HttpResponseBadRequest('Запись в ночное время не разрешена')

        # Если не выбрано ни одно устройство и не установлен флажок аренды, возвращаем ошибку
        if rent_checkbox:
            devices = "АРЕНДА"
        elif devices:
            devices = devices
        else:
            return HttpResponseBadRequest('Выберите хотя бы одно устройство')

            # Проверка поля откуда пришла запись
        if where == '':
            return HttpResponseBadRequest('Не заполнено поле откуда (Это для статистики)')

        # endregion

        # region Получение имени администратора
        admin_name = ""
        try:
            admin = Admins.objects.get(id=int(who))
            admin_name = admin.name
        except Admins.DoesNotExist:
            print("Нет такого админа")
        # endregion

        record = notes_model.objects.create(
            date=date,
            time_from=time_from,
            time_to=time_to,
            devices=devices,
            attendees_count=attendees_count,
            full_name=full_name,
            phone_number=phone_number,
            additional_info=additional_info,
            where=where,
            who=admin_name
        )

        if record is not None:
            add_log(cid=str(club_id), operation="ДОБАВЛЕНИЕ", who=str(admin_name), before="-", after=str(record))
            add_count_note(admin_name, where)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


# Перенос записи
def transfer_record(request):
    if request.method == 'POST':
        noteId = request.POST.get('noteId')
        clubName = request.POST.get('clubName')
        activeAdmin = request.POST.get('activeAdmin')
        mode = request.POST.get('mode')
        selectedClub = request.POST.get('selectedClub')

        if activeAdmin:
            # region получение записи
            notes_model = club_models_notes.get(str(clubName))
            note = notes_model.objects.get(pk=noteId)

            data = {
                'date': str(note.date),
                'time_from': str(note.time_from),
                'time_to': str(note.time_to),
                'devices': note.devices.split(';'),
                'attendees_count': note.attendees_count,
                'full_name': note.full_name,
                'phone_number': note.phone_number,
                'additional_info': note.additional_info,
                'where': note.where,
                'who': note.who,
            }
            # endregion

            # region добавление записи
            notes_model = club_models_notes.get(selectedClub)

            record = notes_model.objects.create(
                date=data['date'],
                time_from=data['time_from'],
                time_to=data['time_to'],
                devices=";".join(data['devices']),
                attendees_count=data['attendees_count'],
                full_name=data['full_name'],
                phone_number=data['phone_number'],
                additional_info=data['additional_info'],
                where=data['where'],
                who=data['who']
            )

            # endregion

            # region удаление записи
            notes_model_for_delete = club_models_notes.get(clubName)
            note_for_delete = get_object_or_404(notes_model_for_delete, id=noteId)
            note_for_delete.delete()
            # endregion

            kuda = "Перенос записи в клуб " + str(selectedClub)
            otkuda = "Перенос записи из клуба " + str(clubName)

            clubID = Club.objects.get(name=clubName)
            clubID_kuda = Club.objects.get(name=selectedClub)

            # region Получение имени администратора
            admin_name = ""
            try:
                admin = Admins.objects.get(id=int(activeAdmin))
                admin_name = admin.name
            except Admins.DoesNotExist:
                print("Нет такого админа")
            # endregion

            # region добавление логов
            add_log(cid=str(clubID.id), operation="ПЕРЕНОС В ДРУГОЙ КЛУБ", who=str(admin_name), before=kuda,
                    after=str(record))
            add_log(cid=str(clubID_kuda.id), operation="ПЕРЕНОС С ДРУГОГО КЛУБА", who=str(admin_name), before=otkuda,
                    after=str(record))
            # endregion

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


# Действие Ушли записи

def delete_record(request):
    if request.method == 'POST':
        # region Получаем данные из запроса
        club_name = request.POST.get('clubName')
        noteId = request.POST.get('noteId')
        clubID = Club.objects.get(name=club_name)
        notes_model = club_models_notes.get(club_name)
        who = request.POST.get('activeAdmin')
        mode = request.POST.get('mode')
        # endregion

        # region Получение имени администратора
        admin_name = ""
        try:
            admin = Admins.objects.get(id=int(who))
            admin_name = admin.name
        except Admins.DoesNotExist:
            print("Нет такого админа")
        # endregion

        # Поиск записи в модели
        note = get_object_or_404(notes_model, id=noteId)

        # Удаление записи
        note.delete()

        if mode == "УШЛИ":
            if noteId:
                add_log(cid=str(clubID.id), operation="УШЛИ", who=str(admin_name), before=str(note), after="-")
        else:
            if noteId:
                add_log(cid=str(clubID.id), operation="ОТМЕНА", who=str(admin_name), before=str(note), after="-")

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


# получение данных записи для окна редактирования
def get_record(request, note_id):
    club_name = request.GET.get('club', None)

    try:
        notes_model = club_models_notes.get(str(club_name))

        # Получаем запись из базы данных по ID
        note = notes_model.objects.get(pk=note_id)

        # Преобразуем данные записи в словарь
        data = {
            'date': str(note.date),
            'time_from': str(note.time_from),
            'time_to': str(note.time_to),
            'devices': note.devices.split(';'),
            'attendees_count': note.attendees_count,
            'full_name': note.full_name,
            'phone_number': note.phone_number,
            'additional_info': note.additional_info,
            'where': note.where,
            'who': note.who,
        }

        return JsonResponse(data)
    except club_name.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)


# страница логов
def logs(request, club_id):
    # Проверяем авторизацию пользователя
    if is_authenticated(request):
        club = Club.objects.get(id=club_id)
        club_name = club.name
        log_model = club_models_log.get(club_name)
        log_list = log_model.objects.all().order_by('-when')

        context = {
            'club': club,
            'club_id': club_id,
            'log_list': log_list,
        }

        return render(request, 'main/log.html', context)


# страница графика
def graph(request, club_id):
    # Проверяем авторизацию пользователя
    if is_authenticated(request):
        club = Club.objects.get(id=club_id)
        club_name = club.name
        graph_model = club_models_graph.get(club_name)

        # Удаляем записи с датой меньше текущей даты
        current_date = datetime.now().date()
        graph_model.objects.filter(date__lt=current_date).delete()

        graph_list = graph_model.objects.all().order_by('date')

        context = {
            'club': club,
            'club_id': club_id,
            'graph_list': graph_list,
        }

        return render(request, 'main/graph.html', context)


# страница статистики
def stat(request, club_id):
    # Проверяем авторизацию пользователя
    if is_authenticated(request):
        # Получаем данные для статистики
        where_info_data = WhereInfo.objects.all().order_by('-counter')
        admins_data = Admins.objects.all().order_by('-counter')

        context = {
            'where_info_data': where_info_data,
            'admins_data': admins_data,
        }

        return render(request, 'main/stat.html', context)


# логи добавление строки
def add_graph_row(request, club_id):
    # Ваша логика для добавления строки

    club = get_object_or_404(Club, id=club_id)
    club_name = club.name
    graph_model = club_models_graph.get(club_name)
    graph_list = graph_model.objects.all().order_by('-date')

    # Получение последней записи, если она существует
    latest_entry = graph_list.first()

    # Вычисление новой даты (если есть последняя запись)
    if latest_entry:
        new_date = latest_entry.date + timedelta(days=1)
    else:
        # Если записей нет, устанавливаем начальную дату (например, сегодняшнюю)
        new_date = date.today()

    # Создание новой записи
    new_entry = graph_model(
        date=new_date,
        Admin_one='',
        Admin_two='',
        Admin_three='',
        Admin_four='',
    )
    new_entry.save()

    # Вместо рендеринга HTML, вернем JSON-ответ
    response_data = {'success': True}
    return JsonResponse(response_data)


# логи сохранение
def save_graph_data(request, club_id):
    if request.method == 'POST':
        try:
            # Получение данных из POST-запроса
            data = request.POST.get('data')
            data = json.loads(data)  # Преобразование строки JSON в Python-объект

            # Получение объекта клуба
            club = get_object_or_404(Club, id=club_id)
            club_name = club.name
            graph_model = club_models_graph.get(club_name)

            # Обработка данных и обновление соответствующих записей
            for entry in data:
                print(entry)
                date_str = entry.get('date')
                admin_one = entry.get('admin_one', '')
                admin_two = entry.get('admin_two', '')
                admin_three = entry.get('admin_three', '')
                admin_four = entry.get('admin_four', '')

                print(date_str)
                date_obj = datetime.strptime(date_str, '%d.%m.%Y')
                print(date_obj)
                # Находим соответствующую запись в модели
                graph_entry = graph_model.objects.filter(date__date=date_obj.date()).first()

                print(graph_entry)

                if graph_entry:
                    # Обновляем данные в модели
                    graph_entry.Admin_one = admin_one
                    graph_entry.Admin_two = admin_two
                    graph_entry.Admin_three = admin_three
                    graph_entry.Admin_four = admin_four
                    graph_entry.save()
                else:
                    # Создаем новую запись, если не найдена существующая
                    graph_model.objects.create(
                        date=date_str,
                        Admin_one=admin_one,
                        Admin_two=admin_two,
                        Admin_three=admin_three,
                        Admin_four=admin_four
                    )

            # Отправляем успешный ответ JSON на клиент
            return JsonResponse({'success': True})

        except Exception as e:
            # Если произошла ошибка, отправляем ответ с ошибкой
            return JsonResponse({'success': False, 'error': str(e)})

    # Если запрос не является POST-запросом, возвращаем ошибку
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


# Добавление лога
def add_log(cid, operation, who, before, after):
    club = Club.objects.get(id=str(cid))
    club_name = club.name
    log_model = club_models_log.get(club_name)
    current_datetime = datetime.now()

    log_entry = log_model.objects.create(
        when=current_datetime,
        who=who,
        operation=operation,
        before=before,
        after=after,
    )

    log_entry.save()


# счётчик при добавлении / статка по типам откуда
def add_count_note(admin, where):
    admin_model = Admins.objects.get(name=str(admin))
    admin_model.counter += 1
    admin_model.save()

    if where == "БЕЗ ЗАПИСИ":
        without_record, created = WhereInfo.objects.get_or_create(where="БЕЗ ЗАПИСИ")
        without_record.counter += 1
    elif where == "ЗВОНОК В КОЛЛ-ЦЕНТР":
        without_record, created = WhereInfo.objects.get_or_create(where="ЗВОНОК В КОЛЛ-ЦЕНТР")
        without_record.counter += 1
    elif where == "ЛИЧНО В КЛУБЕ":
        without_record, created = WhereInfo.objects.get_or_create(where="ЛИЧНО В КЛУБЕ")
        without_record.counter += 1
    elif where == "ЗВОНОК В КЛУБ":
        without_record, created = WhereInfo.objects.get_or_create(where="ЗВОНОК В КЛУБ")
        without_record.counter += 1
    elif where == "СМС":
        without_record, created = WhereInfo.objects.get_or_create(where="СМС")
        without_record.counter += 1
    elif where == "ВК ВИАРЧИК":
        without_record, created = WhereInfo.objects.get_or_create(where="ВК ВИАРЧИК")
        without_record.counter += 1
    elif where == "ВК КИРОВ 1":
        without_record, created = WhereInfo.objects.get_or_create(where="ВК КИРОВ 1")
        without_record.counter += 1
    elif where == "ВК КИРОВ 2":
        without_record, created = WhereInfo.objects.get_or_create(where="ВК КИРОВ 2")
        without_record.counter += 1
    elif where == "ВК ИЖЕВСК":
        without_record, created = WhereInfo.objects.get_or_create(where="ВК ИЖЕВСК")
        without_record.counter += 1
    elif where == "САЙТ КИРОВ":
        without_record, created = WhereInfo.objects.get_or_create(where="САЙТ КИРОВ")
        without_record.counter += 1
    elif where == "САЙТ ИЖЕВСК":
        without_record, created = WhereInfo.objects.get_or_create(where="САЙТ ИЖЕВСК")
        without_record.counter += 1
    elif where == "VIBER":
        without_record, created = WhereInfo.objects.get_or_create(where="VIBER")
        without_record.counter += 1
    elif where == "WHATSAPP":
        without_record, created = WhereInfo.objects.get_or_create(where="WHATSAPP")
        without_record.counter += 1
    elif where == "TELEGRAM":
        without_record, created = WhereInfo.objects.get_or_create(where="TELEGRAM")
        without_record.counter += 1
    elif where == "РАЗВЛЕКАРТА ВК":
        without_record, created = WhereInfo.objects.get_or_create(where="TELEGRAM")
        without_record.counter += 1
    elif where == "ДРУГОЕ (ЛИЧНО)":
        without_record, created = WhereInfo.objects.get_or_create(where="ДРУГОЕ (ЛИЧНО)")
        without_record.counter += 1

    if without_record:
        without_record.save()


# Редактирование записи
def update_record(request, note_id):
    club_name = request.POST.get('club_name')
    notes_model = club_models_notes.get(club_name)
    club = get_object_or_404(Club, name=club_name)
    record = get_object_or_404(notes_model, id=note_id)
    old_record = str(record)
    who = request.POST.get('activeAdmin')

    # region Получение имени администратора
    admin_name = ""
    try:
        admin = Admins.objects.get(id=int(who))
        admin_name = admin.name
    except Admins.DoesNotExist:
        print("Нет такого админа")
    # endregion

    # Обработка POST-запроса для обновления данных
    if request.method == 'POST':
        date = request.POST.get('date')
        time_from = request.POST.get('time_from')
        time_to = request.POST.get('time_to')
        devices = request.POST.get('devices')
        attendees_count = request.POST.get('attendees_count')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        additional_info = request.POST.get('additional_info')
        where = request.POST.get('where_select')

        # region проверки / исправления в нужный формат для таблицы

        if full_name == "":
            full_name = "БЕЗ ИМЕНИ"

        if phone_number == "":
            phone_number = "БЕЗ НОМЕРА"

        if attendees_count == "":
            attendees_count = "-"

        # Проверка / правка наличия даты
        if not date:
            return HttpResponseBadRequest('Не корректная дата')

        # Проверка наличия даты, времени с, времени до и выбранных устройств
        if not time_from:
            return HttpResponseBadRequest('Нет времени с')

        # Проверка наличия времени окончания
        if not time_to:
            # Если время окончания не указано, устанавливаем его как время начала + 3 часа
            time_to = (datetime.strptime(time_from, '%H:%M:%S') + timedelta(hours=3)).strftime('%H:%M:%S')

            # Проверка поля откуда пришла запись
        if where == '':
            return HttpResponseBadRequest('Не заполнено поле откуда (Это для статистики)')

        # Если не выбрано ни одно устройство и не установлен флажок аренды, возвращаем ошибку
        if devices == "":
            return HttpResponseBadRequest('Выберите хотя бы одно устройство')

        # endregion

        # Обновляем данные записи на основе данных из запроса
        record.date = date
        record.time_from = time_from
        record.time_to = time_to
        record.devices = devices
        record.attendees_count = attendees_count
        record.full_name = full_name
        record.phone_number = phone_number
        record.additional_info = additional_info
        record.where = where
        record.save()

        add_log(cid=str(club.id), operation="ИЗМЕНЕНИЕ", who=str(admin_name), before=str(old_record), after=str(record))

        # Возвращаем успешный ответ в формате JSON
        return JsonResponse({'status': 'success'})


# Разделение записи
def separation_record(request, note_id):
    club_name = request.POST.get('club_name')
    notes_model = club_models_notes.get(club_name)
    club = get_object_or_404(Club, name=club_name)
    record = get_object_or_404(notes_model, id=note_id)
    old_record = str(record)
    who = request.POST.get('activeAdmin')

    # region Получение имени администратора
    admin_name = ""
    try:
        admin = Admins.objects.get(id=int(who))
        admin_name = admin.name
    except Admins.DoesNotExist:
        print("Нет такого админа")
    # endregion

    # Обработка POST-запроса для обновления данных
    if request.method == 'POST':
        date = request.POST.get('date')
        time_from = request.POST.get('time_from')
        time_to = request.POST.get('time_to')
        devices = request.POST.get('devices')
        attendees_count = request.POST.get('attendees_count')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        additional_info = request.POST.get('additional_info')
        where = request.POST.get('where_select')

        # region проверки / исправления в нужный формат для таблицы

        if full_name == "":
            full_name = "БЕЗ ИМЕНИ"

        if phone_number == "":
            phone_number = "БЕЗ НОМЕРА"

        if attendees_count == "":
            attendees_count = "-"

        # Проверка / правка наличия даты
        if not date:
            return HttpResponseBadRequest('Не корректная дата')

        # Проверка наличия даты, времени с, времени до и выбранных устройств
        if not time_from:
            return HttpResponseBadRequest('Нет времени с')

        # Проверка наличия времени окончания
        if not time_to:
            # Если время окончания не указано, устанавливаем его как время начала + 3 часа
            time_to = (datetime.strptime(time_from, '%H:%M:%S') + timedelta(hours=3)).strftime('%H:%M:%S')

            # Проверка поля откуда пришла запись
        if where == '':
            return HttpResponseBadRequest('Не заполнено поле откуда (Это для статистики)')

        # Если не выбрано ни одно устройство и не установлен флажок аренды, возвращаем ошибку
        if devices == "":
            return HttpResponseBadRequest('Выберите хотя бы одно устройство')

        # endregion

        new_record = notes_model.objects.create(
            date=date,
            time_from=time_from,
            time_to=time_to,
            devices=devices,
            attendees_count=attendees_count,
            full_name=full_name,
            phone_number=phone_number,
            additional_info=additional_info,
            where=where,
            who=admin_name
        )

        add_log(cid=str(club.id), operation="РАЗБИЕНИЕ", who=str(admin_name), before=str(old_record), after=str(record))

        # Возвращаем успешный ответ в формате JSON
        return JsonResponse({'status': 'success'})


# страница схемы устройств
def scheme(request, club_id):
    if is_authenticated(request):
        # Преобразуем club_id в строку, так как name в модели SettingsSite это строка
        club_id_str = str(club_id)

        club = get_object_or_404(Club, id=club_id)
        club_name = club.name


        # Получаем keys из модели SettingsSite по club_id
        settings_keys = SettingsSite.get_password_by_name(club_id_str)

        sheme_keys_find = 0
        if club_id_str == "1":
            sheme_keys_find = "М102 - схема"
        if club_id_str == "2":
            sheme_keys_find = "МГ51 - схема"
        if club_id_str == "3":
            sheme_keys_find = "Л91 - схема"
        if club_id_str == "4":
            sheme_keys_find = "К40 - схема"
        if club_id_str == "6":
            sheme_keys_find = "АУ1 - схема"
        if club_id_str == "7":
            sheme_keys_find = "У1 - схема"
        if club_id_str == "8":
            sheme_keys_find = "ИЖ - схема"

        scheme_keys = SettingsSite.get_password_by_name(sheme_keys_find)

        context = {
            'club_id': club_id,
            'club_name': club_name,
            'settings_keys': settings_keys,
            'scheme_keys': scheme_keys,
        }

        return render(request, 'main/scheme.html', context)


def generate_soft_color():
    # Генерация случайного цвета с использованием HSL
    h = random.random()  # Hue: 0-1
    s = 0.7  # Saturation: 70%
    l = 0.5  # Lightness: 50%
    return hsl_to_hex(h, s, l)


def hsl_to_hex(h, s, l):
    # Конвертация HSL в RGB
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h * 6) % 2 - 1))
    m = l - c / 2

    r, g, b = 0, 0, 0

    if 0 <= h < 1 / 6:
        r, g, b = c, x, 0
    elif 1 / 6 <= h < 2 / 6:
        r, g, b = x, c, 0
    elif 2 / 6 <= h < 3 / 6:
        r, g, b = 0, c, x
    elif 3 / 6 <= h < 4 / 6:
        r, g, b = 0, x, c
    elif 4 / 6 <= h < 5 / 6:
        r, g, b = x, 0, c
    elif 5 / 6 <= h < 1:
        r, g, b = c, 0, x

    # Конвертируем в диапазон 0-255 и формируем HEX
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return f'#{r:02x}{g:02x}{b:02x}'  # Форматируем в HEX

def scheme_free(request, club_id):
    if is_authenticated(request):
        clubs = Club.objects.all()
        print(clubs)

        club = get_object_or_404(Club, id=club_id)
        club_name = club.name
        notes_model = club_models_notes.get(club_name)
        devices_model = club_models_devices.get(club_name)
        notes = notes_model.objects.all()
        devices = devices_model.objects.all()

        # Отфильтровываем только нужные устройства: "Квесты", "Плойки", "Настолки", "Аренда" и прочее
        filtered_devices = []
        for device in devices:
            if any(key in device.name for key in ['ПЛОЙКА', 'КВЕСТ', 'НАСТОЛКИ', 'АРЕНДА']):
                filtered_devices.append(device)

        # Извлекаем заметки
        extracted_notes = []
        for note in notes:
            devices_list = note.devices.split(';')
            for device in devices_list:
                extracted_notes.append({
                    'date': note.date.strftime('%Y-%m-%d'),
                    'time_from': note.time_from.strftime('%H:%M:%S'),
                    'time_to': note.time_to.strftime('%H:%M:%S'),
                    'devices': device.strip(),
                })

        # Создаем события с названием устройства вместо "Занято"
        extracted_events = []
        for note in extracted_notes:
            extracted_events.append({
                'title': note['devices'],  # Выводим название устройства
                'start': f"{note['date']}T{note['time_from']}",
                'end': f"{note['date']}T{note['time_to']}",
                'color': generate_soft_color(),
            })

        # Создаем события для каждого устройства и объединяем Плойки, Квесты, Настолки и Аренды
        device_events = {'Плойка': [], 'Квест': [], 'Настолки': [], 'Аренда': []}
        for note in extracted_notes:
            if 'ПЛОЙКА' in note['devices']:
                device_events['Плойка'].append({
                    'title': note['devices'],
                    'start': f"{note['date']}T{note['time_from']}",
                    'end': f"{note['date']}T{note['time_to']}",
                    'color': generate_soft_color(),
                })
            elif 'КВЕСТ' in note['devices']:
                device_events['Квест'].append({
                    'title': note['devices'],
                    'start': f"{note['date']}T{note['time_from']}",
                    'end': f"{note['date']}T{note['time_to']}",
                    'color': generate_soft_color(),
                })
            elif 'НАСТОЛКИ' in note['devices']:
                device_events['Настолки'].append({
                    'title': note['devices'],
                    'start': f"{note['date']}T{note['time_from']}",
                    'end': f"{note['date']}T{note['time_to']}",
                    'color': generate_soft_color(),
                })
            elif 'АРЕНДА' in note['devices']:
                device_events['Аренда'].append({
                    'title': note['devices'],
                    'start': f"{note['date']}T{note['time_from']}",
                    'end': f"{note['date']}T{note['time_to']}",
                    'color': generate_soft_color(),
                })
            else:
                # Добавляем устройства, которые не являются Плойками, Квестами, Настолками или Арендой
                if note['devices'] not in device_events:
                    device_events[note['devices']] = []
                device_events[note['devices']].append({
                    'title': note['devices'],
                    'start': f"{note['date']}T{note['time_from']}",
                    'end': f"{note['date']}T{note['time_to']}",
                    'color': generate_soft_color(),
                })

        # Добавляем события "АРЕНДА" во все календари
        for note in extracted_notes:
            if 'АРЕНДА' in note['devices']:
                for key in device_events.keys():
                    device_events[key].append({
                        'title': note['devices'],
                        'start': f"{note['date']}T{note['time_from']}",
                        'end': f"{note['date']}T{note['time_to']}",
                        'color': generate_soft_color(),
                    })

        context = {
            'club_id': club_id,
            'club_name': club_name,
            'devices': filtered_devices,
            'events': device_events,
            'clubs': clubs,
        }

        return render(request, 'main/scheme_free.html', context)


