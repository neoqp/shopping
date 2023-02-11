from django.urls import *

from polls import views

urlpatterns=[
    path('', views.index, name='index'),
]