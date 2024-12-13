from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_exam, name='register_exam'),
    path('confirmation/', views.confirmation_page, name='confirmation'),
]
