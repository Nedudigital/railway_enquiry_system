from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Route



def route_detail(request, rid):
    routes = get_object_or_404(Route, rid=rid)
    return render(request, 'route_detail.html', {'route': routes})
