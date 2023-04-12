from django.urls import path
from dj_app_1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.Users, name="users"),
]