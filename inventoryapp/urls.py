from django.urls import path
from inventoryapp.views import (
    ItemListView,
    ItemCreateView,
    ItemUpdateDelView,
    PurchaseItemCreateView
)

urlpatterns = [
    path('list-item/', ItemListView.as_view()),
    path('create-item/', ItemCreateView.as_view()),
    path('update-del-item/', ItemUpdateDelView.as_view()),
    path('purchase-item/', PurchaseItemCreateView.as_view())
]