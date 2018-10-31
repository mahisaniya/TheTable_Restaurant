from django.conf.urls import url

from booktable import views
app_name="booktable"
urlpatterns = [
    url(r'^$',views.index ,name="booktable"),
]