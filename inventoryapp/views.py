from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework import status, response
from inventoryapp.serializers import ItemSerializer, PurchaseItemSerializer
from inventoryapp.models import Item, PurchaseItem, InvoicePurchaseItem

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateDelView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# class PurchaseItemCreateView(CreateAPIView):
#     queryset = PurchaseItem.objects.all()
#     serializer_class = PurchaseItemSerializer

class PurchaseItemCreateView(APIView):
    serializer_class = PurchaseItemSerializer
    def post(self, request, format=None):
        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid():
        item_list = request.data['item']
        # item_list = serializer.data.get('item')
        # failed_item = []
        success_item_list = []
        for item in item_list:
            success_item = []
            item_available = Item.objects.filter(name=item[0], quantity__lte=item[1])
            if item_available.exists():
                new_quantity = item_available.quantity-item[1]
                item_available.quantity = new_quantity
                item_available.save()
                success_item.append(item[0])
                success_item.append(item[1])
            success_item_list.append(success_item)
            # else:
            #     failed_item.append(item)
        purchase_item = PurchaseItem()
        purchase_item.item = success_item_list
        purchase_item.save() 
        return response.Response({'success':"Purchased."}, status=status.HTTP_201_CREATED)
        # else:        
        #     return response.Response({'failed':"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)
