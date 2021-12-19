from django.urls import path

from . import views

urlpatterns = [
    #l'acceuil
    path('', views.home),
    
]