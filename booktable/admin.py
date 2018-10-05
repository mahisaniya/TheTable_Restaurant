# Register your models here.
from booktable.models import Bookingdetails
from django.contrib import admin


class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'contact', 'date', 'email', 'number_of_guest', 'time')


admin.site.register(Bookingdetails, BookDetailAdmin)