from django.urls import *

from polls import views

urlpatterns=[
    path('', views.index, name='index'),
    path('create/',views.create),
    path('update/',views.update),
    path('delete/',views.delete),
]