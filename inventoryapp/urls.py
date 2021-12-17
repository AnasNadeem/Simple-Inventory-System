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
    PurchaseItemCreateView,
    PurchaseItemListView,
)

urlpatterns = [
    path('list-item/', ItemListView.as_view()),
    path('create-item/', ItemCreateView.as_view()),
    path('update-item/<int:pk>/', ItemUpdateView.as_view()),
    path('delete-item/<int:pk>/', ItemDeleteView.as_view()),
    path('purchase-item-list/', PurchaseItemListView.as_view()),
    path('purchase-item/', PurchaseItemCreateView.as_view()),
    path('list-customer/', CustomerListView.as_view()),
    path('create-customer/', CustomerCreateView.as_view()),
    path('update-customer/<int:pk>/', CustomerUpdateView.as_view()),
    path('delete-customer/<int:pk>/', CustomerDeleteView.as_view()),

]