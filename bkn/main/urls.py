# main/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('club_page', club_page, name='club_page'),
    path('get_notes_data/<str:club_id>/', get_notes_data, name='get_notes_data'),
    path('save_record/', save_record, name='save_record'),
    path('transfer_record/', transfer_record, name='transfer_record'),
    path('get_phone_number_data/', get_phone_number_data, name='get_phone_number_data'),
    path('save_warning_info/', save_warning_info, name='save_warning_info'),
    path('delete_record/', delete_record, name='delete_record'),
    path('get_record/<int:note_id>/', get_record, name='get_record'),
    path('logs/<str:club_id>/', logs, name='logs'),
    path('graph/<str:club_id>/', graph, name='graph'),
    path('stat/<str:club_id>/', stat, name='stat'),
    path('scheme/<str:club_id>/', scheme, name='scheme'),
    path('scheme_free/<str:club_id>/', scheme_free, name='scheme_free'),
    path('place_device/<str:club_id>/', place_device, name='place_device'),
    path('assign_place/<int:club_id>/<int:game_id>/', assign_place, name='assign_place'),
    path('edit_games/<int:club_id>/<int:game_id>/update_assignments/', update_assignments, name='update_assignments'),
    path('edit_games/<str:club_id>/', edit_games, name='edit_games'),

    path('add_graph_row/<int:club_id>/', add_graph_row, name='add_graph_row'),
    path('save_graph_data/<int:club_id>/', save_graph_data, name='save_graph_data'),
    path('update_record/<int:note_id>/', update_record, name='update_record'),
    path('separation_record/<int:note_id>/', separation_record, name='separation_record'),

]
