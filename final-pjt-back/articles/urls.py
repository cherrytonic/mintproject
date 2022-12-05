from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getticketlists,name='getticketlists'),
    path('create/',views.createticketlist,name='createticketlist'),
    path('<int:ticketlist_pk>/',views.getticketlist,name='getticketlist'),
    path('<int:ticketlist_pk>/comment/',views.createcomment,name='createcomment'),
    path('<int:ticketlist_pk>/comment/<int:comment_pk>',views.deletecomment,name='deletecomment'),
    path('<int:ticketlist_pk>/getcomment/',views.getcomment,name='getcomment'),
    path('<int:ticketlist_pk>/likes/',views.likes,name='likes'),
    path('<int:ticketlist_pk>/getlikes/<str:username>',views.getlikes,name='getlikes'),
]