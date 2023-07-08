from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Route



def route_list(request):
    routes = Route.objects.all()
    return render(request, 'route.list.html', {'routes': routes})
