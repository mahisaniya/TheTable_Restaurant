# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
admin.site.register(Event,EventAdmin)