from django.shortcuts import render, get_object_or_404, redirect
from railway_app.models import Payment
from railway_app.forms import PaymentForm



def payment_detail(request, pnr):
    payments = get_object_or_404(Payment, pnr=pnr)
    return render(request, 'payment_detail.html', {'payments': payments})
