from django.http import HttpResponse
from django.shortcuts import render
from booktable.forms import Bookingforms
from django.contrib import messages
from .models import Bookingdetails

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = Bookingforms(request.POST)
        if form.is_valid():
            table=form.save()
            customer_name=form.cleaned_data['customer_name']
            contact=form.cleaned_data['contact']
            date=form.cleaned_data['date']
            email=form.cleaned_data['email']
            number_of_guest=form.cleaned_data['number_of_guest']
            time=form.cleaned_data['time']
            table.save()
            messages.success(request ,'your table has booked')
    else:
        form = Bookingforms()
    return render(request,'booktable/booking.html', {'form':form})