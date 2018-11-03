from django.conf.urls import url, include
from django.urls import path
from operators import views

app_name = 'operators'
urlpatterns = [
        url(r'newoperator/$', views.get_operators, name='new_operator'),


    ]
