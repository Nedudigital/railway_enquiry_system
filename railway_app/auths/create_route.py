from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Route
from railway_app.forms import RouteForm
# Create your views here.




def create_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_app:route_list')
    else:
        form = RouteForm()
    return render(request, 'create_route.html', {'form': form})
