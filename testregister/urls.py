from django.urls import path
from . import views

urlpatterns = [
    path('testregister/', views.whenTest, name='select')
]