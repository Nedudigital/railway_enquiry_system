from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from railway_app.models import Trains
from railway_app.forms import SearchForm




def search_trains(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            src = form.cleaned_data['source']
            des = form.cleaned_data['destination']
            date = form.cleaned_data['date']


        #retrive train schedules based on user input from the Train model
        trains = Trains.objects.filter(route__ostation=src, route__dstation=des)


        context = {
            'train': trains,
            'source': src,
            'destination': des,
            'date': date,
        }
    else:
        form = SearchForm()

    return render(request, 'search_trains.html', {'form': form})
