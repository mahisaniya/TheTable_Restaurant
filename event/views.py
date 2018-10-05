# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from  .models import Event

# Create your views here.
def events (request):
    #text="hello"
    all_event=Event.objects.all()
    return render(request , 'event/event.html', {'all_event': all_event})
    #return HttpResponse(text)