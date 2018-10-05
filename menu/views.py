

from django.shortcuts import render
from .models import Menu , SubMenu


# Create your views here.
def menu(request):
    all_menu = Menu.objects.all()
    return render(request,'menu/menu.html',{'all_menu':all_menu})

def sub_menu(request):
    all_sub_menu = SubMenu.objects.all()
    all_menu = Menu.objects.all()
    return render(request ,'menu/sub_menu.html',{'all_sub_menu':all_sub_menu,'all_menu':all_menu})

