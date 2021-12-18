from django.urls import path
from inventoryapp.views import (
    # Item Get, Post, Update, Delete
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    # Customer Get, Post, Update, Delete
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    # PurchaseItem
    PurchaseItemListView,
    PurchaseItemCreateUpdateView,
    PurchaseItemDeleteView
)

urlpatterns = [
    # Item urls 
    path('list-item/', ItemListView.as_view()),
    path('create-item/', ItemCreateView.as_view()),
    path('update-item/<int:pk>/', ItemUpdateView.as_view()),
    path('delete-item/<int:pk>/', ItemDeleteView.as_view()),
    # Customer urls 
    path('list-customer/', CustomerListView.as_view()),
    path('create-customer/', CustomerCreateView.as_view()),
    path('update-customer/<int:pk>/', CustomerUpdateView.as_view()),
    path('delete-customer/<int:pk>/', CustomerDeleteView.as_view()),
    # Purchase item urls 
    path('list-puritem/', PurchaseItemListView.as_view()),
    path('create-puritem/', PurchaseItemCreateUpdateView.as_view()),
    path('update-puritem/<int:pk>/', PurchaseItemCreateUpdateView.as_view()),
    path('delete-puritem/<int:pk>/', PurchaseItemDeleteView.as_view()),
]