from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('genres/', views.genres_list),
]