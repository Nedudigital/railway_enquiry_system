from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Trains


def train_detail(request, tno):
    train = get_object_or_404(Trains, tno=tno)
    return render(request, 'train_detail.html', {'train': train})
