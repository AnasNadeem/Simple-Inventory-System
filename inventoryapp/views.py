from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework import status, response
from inventoryapp.serializers import ItemSerializer, PurchaseItemSerializer
from inventoryapp.models import Item, PurchaseItem, InvoicePurchaseItem
import json
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateDelView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PurchaseItemListView(ListAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

