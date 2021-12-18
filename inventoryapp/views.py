from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status, response
from inventoryapp.serializers import (
    ItemSerializer, 
    CustomerSerializer,
    PurchaseItemSerializer,
    PurchaseItemViewSerializer)
from inventoryapp.models import (
    Item,
    PurchaseItem, 
    InvoicePurchaseItem, 
    Customer)

# Checked 
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Checked 
class ItemCreateView(APIView):
    serializer_class = ItemSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            item_name = serializer.data.get('name')
            item_price = serializer.data.get('price')
            item_quantity = serializer.data.get('quantity')
            item_description = serializer.data.get('description')
            item = Item.objects.filter(name=item_name, price=item_price)
            if len(item)>0:
                return response.Response({"error":"Item already exist."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                new_item = Item()
                new_item.name = item_name
                new_item.price = item_price
                new_item.quantity = item_quantity
                new_item.description = item_description
                new_item.save()
                return response.Response({"success":"Item added."}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class ItemUpdateView(APIView):
    serializer_class = ItemSerializer
    def put(self, request, pk, format=None):
        item = Item.objects.filter(id=pk)
        if len(item)>0:
            item = item[0]
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                item_name = serializer.data.get('name')
                item_price = serializer.data.get('price')
                item_quantity = serializer.data.get('quantity')
                item_description = serializer.data.get('description')
                item.name = item_name
                item.price = item_price
                item.quantity = item_quantity
                item.description = item_description
                item.save()
                return response.Response({"success":"Item updated."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)     
        else:
            return response.Response({"error":"Invalid item."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class ItemDeleteView(APIView):
    def delete(self,request, pk, format=None):
        item = Item.objects.filter(id=pk)
        if len(item)>0:
            item = item[0]
            item.delete()
            return response.Response({"success":"Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid item."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#Checked
class CustomerCreateView(APIView):
    serializer_class = CustomerSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cus_name = serializer.data.get('name')
            cus_number = serializer.data.get('phone_num')
            cus_address = serializer.data.get('address')
            customer = Customer.objects.filter(phone_num=cus_number)
            if len(customer)>0:
                return response.Response({"error":"Customer with that number already exist."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                new_cus = Customer()
                new_cus.name = cus_name
                new_cus.phone_num = cus_number
                new_cus.address = cus_address
                new_cus.save()
                return response.Response({"success":"Customer added."}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)

# Checked
class CustomerUpdateView(APIView):
    serializer_class = CustomerSerializer
    def put(self, request, pk, format=None):
        customer = Customer.objects.filter(id=pk)
        if len(customer)>0:
            customer = customer[0]
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                cus_name = serializer.data.get('name')
                cus_number = serializer.data.get('phone_num')
                cus_address = serializer.data.get('address')
                customer.name = cus_name
                customer.phone_num = cus_number
                customer.address = cus_address
                customer.save()
                return response.Response({"success":"Customer updated."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)     
        else:
            return response.Response({"error":"Invalid customer."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class CustomerDeleteView(APIView):
    def delete(self, request, pk, format=None):
        customer = Customer.objects.filter(id=pk)
        if len(customer)>0:
            customer = customer[0]
            customer.delete()
            return response.Response({"success":"Customer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid Customer."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class PurchaseItemListView(ListAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemViewSerializer

# Checked 
class PurchaseItemCreateUpdateView(APIView):
    serializer_class = PurchaseItemSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cus_id = serializer.data.get('customer')
            item_id = serializer.data.get('item')
            quantity = serializer.data.get('quantity')
            customer = Customer.objects.filter(id=cus_id)
            if len(customer)>0:
                return self.check_item_and_quantity(cus_id=cus_id,item_id=item_id,quantity=quantity)
                # return response.Response({'success':f"Purchase item created."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"No such customer exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        purchase_item = PurchaseItem.objects.filter(id=pk)
        if len(purchase_item)>0:
            purchase_item = purchase_item[0]
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                cus_id = serializer.data.get('customer')
                item_id = serializer.data.get('item')
                quantity = serializer.data.get('quantity')
                customer = Customer.objects.filter(id=cus_id)
                if len(customer)>0:
                    self.check_item_and_quantity(cus_id=cus_id,item_id=item_id,quantity=quantity,put_pur_item=purchase_item)
                    return response.Response({'success':f"Purchase item updated."}, status=status.HTTP_201_CREATED)
                else:
                    return response.Response({"error":"No such customer exists."}, status=status.HTTP_400_BAD_REQUEST)                
            else:
                return response.Response({"error":"Invalid data."}, status=status.HTTP_400_BAD_REQUEST)     
        else:
            return response.Response({"error":"Invalid Purchase Item."}, status=status.HTTP_400_BAD_REQUEST)

    def check_item_and_quantity(self, cus_id, item_id, quantity, put_pur_item=''):
        item = Item.objects.filter(id=item_id)
        if len(item)>0:
            item = item[0]
            if quantity<=item.quantity:
                new_quantity = item.quantity - quantity
                item.quantity=new_quantity
                item.save()
                if put_pur_item:
                    put_pur_item.customer=Customer.objects.get(id=cus_id)
                    put_pur_item.item=item
                    put_pur_item.quantity=quantity
                    put_pur_item.save()
                    return response.Response({'success':f"Purchase item created."}, status=status.HTTP_201_CREATED)
                else:
                    purchase_item = PurchaseItem()
                    purchase_item.customer=Customer.objects.get(id=cus_id)
                    purchase_item.item=item
                    purchase_item.quantity=quantity
                    purchase_item.save()
            else:
                return response.Response({"error":"Quantity failure."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"No such item exists."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class PurchaseItemDeleteView(APIView):
    def delete(self, request, pk, format=None):
        purchase_item = PurchaseItem.objects.filter(id=pk)
        if len(purchase_item)>0:
            purchase_item = purchase_item[0]
            purchase_item.delete()
            return response.Response({"success":"PurchaseItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid PurchaseItem."}, status=status.HTTP_400_BAD_REQUEST)
