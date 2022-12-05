from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('user/all/', views.getAllUser, name='getAllUser'),
    path('user/<int:user_pk>/', views.getUser, name='getUser'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('getUserdata/<str:username>/', views.getUserData, name='getUserData'),
]
