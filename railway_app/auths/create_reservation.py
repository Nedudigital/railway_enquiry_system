from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Reservation
from railway_app.forms import ReservationForm
# Create your views here.




def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_app:reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form})
