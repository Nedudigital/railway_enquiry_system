from django.urls import path
# from . import views
from .auths import ( create_train, create_route, create_station, create_reservation, create_payment,
                train_list, train_detail, station_list, station_detail, route_list, route_detail,
                reservation_list, reservation_detail, payment_list, payment_detail, ticket_confirmation,
                book_ticket, search_trains
        )


app_name = 'railway_app'

urlpatterns = [

    path('create/trains/', create_train.create_train, name='create_train'),
    path('create/route/', create_route.create_route, name='create_route'),
    path('create/station/', create_station.create_station, name='create_station'),
    path('create/reservation/', create_reservation.create_reservation, name='create_reservation'),
    path('create/payment/', create_payment.create_payment, name='create_payment'),

    path('trains/', train_list.train_list, name='train_list'),
    path('trains/<str:tno>/', train_detail.train_detail, name='train_detail'),

    path('stations/', station_list.station_list, name='station_list'),
    path('stations/<str:sid>/', station_detail.station_detail, name='station_detail'),

    path('routes/', route_list.route_list, name='route_list'),
    path('routes/<str:rid>/', route_detail.route_detail, name='route_detail'),

    path('reservations/', reservation_list.reservation_list, name='reservation_list'),
    path('reservations/<str:pnr>/', reservation_detail.reservation_detail, name='reservation_detail'),

    path('payments/', payment_list.payment_list, name='payment_list'),
    path('payments/<str:pnr>/', payment_detail.payment_detail, name='payment_detail'),


    path('confirmation/<str:pnr>/', ticket_confirmation.ticket_confirmation, name='ticket_confirmation'),

    path('book/<str:tno>/', book_ticket.book_ticket, name='book_ticket'),

    path('search/', search_trains.search_trains, name='search_trains'),





















    # path('trains/', views.train_list, name='train_list'),
    # path('trains/<str:tno>/', views.train_detail, name='train_detail'),
    # path('routes/', views.route_list, name='route_list'),
    # path('routes/<str:rid>/', views.route_detail, name='route_detail'),
    # path('stations/', views.station_list, name='station_list'),
    # path('stations/<str:sid>/', views.station_detail, name='station_detail'),
    # path('reservations/', views.reservation_list, name='reservation_list'),
    # path('reservations/<str:pnr>/', views.reservation_detail, name='reservation_detail'),
    # path('payments/', views.payment_list, name='payment_list'),
    # path('payments/<str:pnr>/', views.payment_detail, name='payment_detail'),
    # path('create/trains/', views.create_train, name='create_train'),
    # path('create/route/', views.create_route, name='create_route'),
    # path('create/station/', views.create_station, name='create_station'),
    # path('create/reservation/', views.create_reservation, name='create_reservation'),
    # path('create/payment/', views.create_payment, name='create_payment'),
    # path('search/', views.search_trains, name='search_trains'),
    # path('book/<str:tno>/', views.book_ticket, name='book_ticket'),
    # path('confirmation/<str:pnr>/', views.ticket_confirmation, name='ticket_confirmation')

]
