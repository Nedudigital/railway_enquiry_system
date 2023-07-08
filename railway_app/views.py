# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .models import Trains, Route, Station, RouteStation, Reservation, Payment
# from .forms import TrainsForm, RouteForm, StationForm, ReservationForm, PaymentForm, SearchForm
# Create your views here.
#
# def create_train(request):
#     if request.method == 'POST':
#         form = TrainsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('railway_app:train_list')
#         else:
#             form = TrainsForm()
#         return render(request, 'create_train.html', {'form': form})
#
#
# def create_route(request):
#     if request.method == 'POST':
#         form = RouteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('railway_app:route_list')
#         else:
#             form = RouteForm()
#         return render(request, 'create_route.html', {'form': form})
#
#
# def create_station(request):
#     if request.method == 'POST':
#         form = StationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('railway_app:station_list')
#         else:
#             form = StationForm()
#         return render(request, 'create_station.html', {'form': form})
#
# def create_reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('railway_app:reservation_list')
#         else:
#             form = ReservationForm()
#         return render(request, 'create_reservation.html', {'form': form})
#
#
# def create_payment(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('railway_app:payment_list')
#         else:
#             form = PaymentForm()
#         return render(request, 'create_payment.html', {'form': form})
#
#
#
#
#
#
# def train_list(request):
#     trains = Trains.objects.all()
#     return render(request, 'train_list.html', {'trains': trains})
#
# def train_detail(request, tno):
#     train = get_object_or_404(Trains, tno=tno)
#     return render(request, 'train_detail.html', {'train': train})
#
# def route_list(request):
#     routes = Route.objects.all()
#     return render(request, 'route.list.html', {'routes': routes})
#
# def route_detail(request, rid):
#     routes = get_object_or_404(Route, rid=rid)
#     return render(request, 'route_detail.html', {'route': routes})
#
# def station_list(request):
#     stations = Station.objects.all()
#     return render(request, 'station_list.html', {'stations': stations})
#
# def station_detail(request, sid):
#     stations = get_object_or_404(Station, sid=sid)
#     return render(request, 'station_detail.html', {'stations': stations})
#
# def reservation_list(request):
#     reservations = Reservation.objects.all()
#     return render(request, 'reservation_list.html', {'reservations': reservations})
#
# def reservation_detail(request, pnr):
#     reservations = get_object_or_404(Reservation, pnr=pnr)
#     return render(request, 'reservation_detail.html', {'reservations': reservations})
#
# def payment_list(request):
#     payments = Payment.objects.all()
#     return render(request, 'payment_list.html', {'payments': payments})
#
# def payment_detail(request, pnr):
#     payments = get_object_or_404(Payment, pnr=pnr)
#     return render(request, 'payment_detail.html', {'payments': payments})


# def search_trains(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             src = form.cleaned_data['source']
#             des = form.cleaned_data['destination']
#             date = form.cleaned_data['date']
#
#
#         #retrive train schedules based on user input from the Train model
#         trains = Trains.objects.filter(route__ostation=src, route__dstation=des)
#
#
#         context = {
#             'trains': trains,
#             'source': src,
#             'destination': des,
#             'date': date,
#         }
#         return render(request, 'search_trains.html', {'form': form})
# 
#
#
# def book_ticket(request, tno):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.tno = Trains.objects.get(tno=tno)
#             reservation.save()
#             return redirect('railway_app:ticket_confirmation', pnr=reservation.pnr)
#     else:
#         form = ReservationForm()
#     return render(request, 'book_ticket.html', {'form': form, 'tno': tno})
#
#
# def ticket_confirmation(request, pnr):
#     reservation = Reservation.objects.get(pnr=pnr)
#     return render(request, 'ticket_confirmation.html', {'reservation': reservation})
