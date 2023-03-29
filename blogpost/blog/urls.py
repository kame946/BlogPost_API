from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.blogpost_list),
    path('create/', views.blogpost_detail),
    path('create/<int:pk>/', views.blogpost_detail),
]
