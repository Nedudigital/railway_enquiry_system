from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Station
from railway_app.forms import StationForm
# Create your views here.



def create_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_app:station_list')
    else:
        form = StationForm()
    return render(request, 'create_station.html', {'form': form})
