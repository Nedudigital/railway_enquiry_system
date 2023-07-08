from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Trains

def train_list(request):
    trains = Trains.objects.all()
    return render(request, 'train_list.html', {'trains': trains})
