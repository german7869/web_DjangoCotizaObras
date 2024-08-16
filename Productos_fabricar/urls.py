from django.urls import path
from . import views

urlpatterns = [
    path('productosF/', views.productos, name="listado productos"),
   
]