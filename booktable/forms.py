
from django import forms

# from django.apps import apps
from .models import Bookingdetails


class Bookingforms(forms.ModelForm):
    class Meta:
        model = Bookingdetails
        fields = ['customer_name', 'contact', 'date', 'email', 'number_of_guest', 'time']