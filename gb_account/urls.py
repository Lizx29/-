from django.urls import path, include
from gb_account import views

urlpatterns = [
    path('', views.index),
]