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
    # PurchaseItem Get, Post, Update, Delete
    PurchaseItemListView,
    PurchaseItemOrderedListView,
    PurchaseItemUnOrderedListView,
    PurchaseItemCreateView,
    PurchaseItemUpdateView,
    PurchaseItemDeleteView,
    PurchaseItemCustomerListView,
    # InvoicePurchaseItem Get, Post, Delete
    InvoicePurchaseItemListView,
    InvoicePurchaseItemCreateView,
    # InvoicePurchaseItemDeleteView,
    InvoicePurchaseItemView
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
    path('list-orderedpuritem/', PurchaseItemOrderedListView.as_view()),
    path('list-unorderedpuritem/', PurchaseItemUnOrderedListView.as_view()),
    path('list-puritem/<customer>/', PurchaseItemCustomerListView.as_view()),
    path('create-puritem/', PurchaseItemCreateView.as_view()),
    path('update-puritem/<int:pk>/', PurchaseItemUpdateView.as_view()),
    path('delete-puritem/<int:pk>/', PurchaseItemDeleteView.as_view()),
    # Invoice purchase item urls 
    path('list-invpuritem/', InvoicePurchaseItemListView.as_view()),
    path('create-invpuritem/', InvoicePurchaseItemCreateView.as_view()),
    # path('delete-invpuritem/<int:pk>/', InvoicePurchaseItemDeleteView.as_view()),
    path('get-invoice/<int:pk>/', InvoicePurchaseItemView.as_view()),
]

