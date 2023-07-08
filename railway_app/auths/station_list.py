from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Station




def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations': stations})
