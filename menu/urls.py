from django.conf.urls import url
from menu import views
app_name ='menu'
urlpatterns=[
    #url(r'^$',views.menu, name='menu'),

    url(r'^$',views.sub_menu , name='menu')
]
