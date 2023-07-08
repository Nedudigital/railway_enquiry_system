from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Station




def station_detail(request, sid):
    stations = get_object_or_404(Station, sid=sid)
    return render(request, 'station_detail.html', {'stations': stations})
