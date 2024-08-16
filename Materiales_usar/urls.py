from django.urls import path
from . import views

urlpatterns = [
    path('materiales/', views.materiales, name="mateirales"),
   
]