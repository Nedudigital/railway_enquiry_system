from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Trains
from railway_app.forms import ReservationForm




def book_ticket(request, tno):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.tno = Trains.objects.get(tno=tno)
            reservation.save()
            return redirect('railway_app:ticket_confirmation', pnr=reservation.pnr)
    else:
        form = ReservationForm()
    return render(request, 'book_ticket.html', {'form': form, 'tno': tno})
