from django.urls import *
from navbar import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('bar/', views.bar),
]