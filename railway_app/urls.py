from django.urls import path
from . import views

app_name = 'railway_app'

urlpatterns = [
    path('trains/', views.train_list, name='train_list'),
    path('trains/<str:tno>/', views.train_detail, name='train_detail'),
    path('routes/', views.route_list, name='route_list'),
    path('routes/<str:rid>/', views.route_detail, name='route_detail'),
     path('stations/', views.station_list, name='station_list'),
    path('stations/<str:sid>/', views.station_detail, name='station_detail'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/<str:pnr>/', views.reservation_detail, name='reservation_detail'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/<str:pnr>/', views.payment_detail, name='payment_detail'),
    path('create/trains/', views.create_train, name='create_train'),
    path('create/route/', views.create_route, name='create_route'),
    path('create/station/', views.create_station, name='create_station'),
    path('create/reservation/', views.create_reservation, name='create_reservation'),
    path('create/payment/', views.create_payment, name='create_payment'),
    path('search/', views.search_trains, name='search_trains'),
    path('book/<str:tno>/', views.book_ticket, name='book_ticket'),
    path('confirmation/<str:pnr>/', views.ticket_confirmation, name='ticket_confirmation')

]