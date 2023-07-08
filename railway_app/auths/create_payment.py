from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Payment
from railway_app.forms import PaymentForm
# Create your views here.




def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_app:payment_list')
    else:
        form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form})
