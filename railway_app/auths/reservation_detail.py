from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Reservation




def reservation_detail(request, pnr):
    reservations = get_object_or_404(Reservation, pnr=pnr)
    return render(request, 'reservation_detail.html', {'reservations': reservations})
