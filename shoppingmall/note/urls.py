from django.urls import *
from . import views

app_name="note"

urlpatterns=[
    path('create/', views.create, name='create'),
    path('', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]