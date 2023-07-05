from django import forms
from .models import Trains, Route, Station, Reservation, Payment

class TrainsForm(forms.ModelForm):
    class Meta:
        model = Trains
        fields = '__all__'

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__' 

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class   PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'        

class SearchForm(forms.Form):
    src = forms.CharField(label='Source', max_length=50)
    des = forms.CharField(label='Destination', max_length=50)
    date = forms.DateField(label='Date')
           