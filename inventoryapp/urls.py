from django.urls import path
from inventoryapp.views import home

urlpatterns = [
    path('', home)
]