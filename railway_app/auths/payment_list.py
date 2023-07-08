from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Payment
from railway_app.forms import PaymentForm



def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})
