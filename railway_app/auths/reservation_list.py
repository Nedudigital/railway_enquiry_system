from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Reservation


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})
