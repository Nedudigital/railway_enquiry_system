from django.shortcuts import render, get_object_or_404

from railway_app.models import Trains
from railway_app.forms import TrainsForm



def create_train(request):
    if request.method == 'POST':
        form = TrainsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_app:train_list')
    else:
        form = TrainsForm()
    return render(request, 'create_train.html', {'form': form})
