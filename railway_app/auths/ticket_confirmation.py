from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Reservation





def ticket_confirmation(request, pnr):
    reservation = Reservation.objects.get(pnr=pnr)
    return render(request, 'ticket_confirmation.html', {'reservation': reservation})
