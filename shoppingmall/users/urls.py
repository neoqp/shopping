from django.urls import *
from django.contrib.auth import views as auth_views
import users.views

app_name="users"
urlpatterns=[
    path('login/',users.views.login, name='login'),
    path('signup/',users.views.signup, name='signup'),
    path('logout/',users.views.logout, name='logout'),
]