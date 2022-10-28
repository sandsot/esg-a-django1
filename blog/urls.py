from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('new/', views.post_new),
    path('restaurants', views.restaurant_index),
    path('restaurants/<int:pk>/', views.res_post_page),
    path('restaurants/new/', views.res_new),
]