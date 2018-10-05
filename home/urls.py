from django.conf.urls import url
from home import views

app_name = 'home'
urlpatterns =[
    url('^$', views.index, name='home')
]
