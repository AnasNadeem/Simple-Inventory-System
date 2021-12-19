from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status, response
from inventoryapp.serializers import (
    ItemSerializer, 
    CustomerSerializer,
    PurchaseItemSerializer,
    PurchaseItemViewSerializer,
    InvoicePurchaseItemSerializer)
from inventoryapp.models import (
    Item,
    PurchaseItem, 
    InvoicePurchaseItem, 
    Customer)
from inventoryapp.pdfgen import GenereatePdf
# Checked 
class ItemListView(ListAPIView):
    """GET - All the Items."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Checked 
class ItemCreateView(APIView):
    """POST - Create Item with name price quantity and description."""
    serializer_class = ItemSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            item_name = serializer.data.get('name')
            item_price = serializer.data.get('price')
            item_quantity = serializer.data.get('quantity')
            item_description = serializer.data.get('description')
            # Checking if the item already exists
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
    """PUT - Update Item with name price quantity and description."""
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
    """DELETE - Delete Item by their id."""
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
    """GET - All the Customer."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#Checked
class CustomerCreateView(APIView):
    """POST - Create Customer with name number and address."""
    serializer_class = CustomerSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cus_name = serializer.data.get('name')
            cus_number = serializer.data.get('phone_num')
            cus_address = serializer.data.get('address')
            # Checking if the customer with that number already exists 
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
    """PUT - Update Customer with name number and address."""
    serializer_class = CustomerSerializer
    def put(self, request, pk, format=None):
        # Checking if the customer exists 
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
    """DELETE - Delete Customer by their id."""
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
    """GET - All the PurchaseItem."""
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemViewSerializer

# Checked
class PurchaseItemCreateView(APIView):
    """POST - Create PurchaseItem with customer item and quantity."""
    serializer_class = PurchaseItemSerializer
    def post(self, request, format=None):
        cus_id = request.data['customer']
        item_id = request.data['item']
        quantity = request.data['quantity']
        # Checking if the customer exist
        customer = Customer.objects.filter(pk=cus_id)
        if len(customer)>0:
            # Checking if the item exist
            item = Item.objects.filter(pk=item_id)
            if len(item)>0:
                item = item[0]
                # Checking if PurchaseItem with that Item and Customer already exist
                purchase_item = PurchaseItem.objects.filter(customer=customer[0].id, item=item.id)
                if purchase_item.exists():
                    return response.Response({"error":"Purchaseitem with that list already exists. Use PUT."}, status=status.HTTP_400_BAD_REQUEST)    
                else:
                    # Checking if the item of this quantity is available 
                    if quantity<=item.quantity:
                        # Creating Purchase Item
                        new_purchase_item = PurchaseItem()
                        new_purchase_item.customer = customer[0]
                        new_purchase_item.item = item
                        new_purchase_item.quantity = quantity
                        new_purchase_item.save()
                        # Updating the Item model
                        new_quantity = item.quantity-quantity
                        item.quantity = new_quantity
                        item.save()
                        return response.Response({"success":"PurchaseItem created."}, status=status.HTTP_201_CREATED)
                    else:
                        return response.Response({"error":"Quantity failure."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response.Response({"error":"No such item exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"No such customer exists."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class PurchaseItemUpdateView(APIView):
    """PUT - Update PurchaseItem with customer item and quantity."""
    serializer_class = PurchaseItemSerializer
    def put(self, request, pk, format=None):
        # Checking if the PurchaseItem exist or not
        purchase_item = PurchaseItem.objects.filter(pk=pk)
        if len(purchase_item)>0:
            purchase_item = purchase_item[0]
            cus_id = request.data['customer']
            item_id = request.data['item']
            quantity = request.data['quantity']
            # Checking if the customer exist
            customer = Customer.objects.filter(pk=cus_id)
            if len(customer)>0:
                # Checking if the item exist
                item = Item.objects.filter(pk=item_id)
                if len(item)>0:
                    item = item[0]
                    if quantity<=item.quantity:  
                        if purchase_item.quantity >= quantity:
                            # Updating the Item model quantity 
                            new_quantity = item.quantity + (purchase_item.quantity - quantity)
                            item.quantity = new_quantity
                            item.save()
                        else:
                            # Updating the Item model quantity 
                            new_quantity = item.quantity - (quantity - purchase_item.quantity)
                            item.quantity = new_quantity
                            item.save()
                        # Updating the PurchaseItem quantity 
                        purchase_item.quantity=quantity
                        purchase_item.save()
                        return response.Response({"success":"PurchaseItem updated."}, status=status.HTTP_201_CREATED)
                    else:
                        return response.Response({"error":"Quantity failure."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return response.Response({"error":"No such item exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response.Response({"error":"No such customer exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"Invalid Purchase Item."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class PurchaseItemDeleteView(APIView):
    """DELETE - Delete PurchaseItem by their id."""
    def delete(self, request, pk, format=None):
        purchase_item = PurchaseItem.objects.filter(id=pk)
        if len(purchase_item)>0:
            purchase_item = purchase_item[0]
            purchase_item.delete()
            return response.Response({"success":"PurchaseItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid PurchaseItem."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class InvoicePurchaseItemListView(ListAPIView):
    """GET - List of all Invoice"""
    queryset = InvoicePurchaseItem.objects.all()
    serializer_class = InvoicePurchaseItemSerializer

class InvoicePurchaseItemCreateView(APIView):
    """POST - Create Invoice of Purchase Item."""
    def post(self, request, format=None):
        customer_id = request.data['customer']
        # Check if customer exists
        customer = Customer.objects.filter(pk=customer_id)
        if len(customer)>0:
            customer = customer[0]
            # Checking for PurchaseItem 
            purchase_item_list = PurchaseItem.objects.filter(customer=customer.id)
            if len(purchase_item_list)>0:
                inv_pur_item = InvoicePurchaseItem()
                inv_pur_item.customer = customer
                inv_pur_item.save()
                all_prod_list = []
                total_price = 0
                for purchase_item in purchase_item_list:
                    item = Item.objects.get(pk=purchase_item.item.id)
                    prod_list = []
                    prod_list.append(item.name)
                    prod_list.append(item.price)
                    prod_list.append(purchase_item.quantity)
                    item_price = item.price * purchase_item.quantity
                    total_price+=item_price
                    prod_list.append(item_price)
                    all_prod_list.append(prod_list)
                    # Inserting PurchaseItem in InvoicePurchaseItem 
                    inv_pur_item.purchase_item.add(purchase_item)
                # File Name and location
                exact_file_name = f"media/{inv_pur_item.id}_{customer.name}_{total_price}"
                # Insert the pdf into database 
                # inv_pur_item.invoice = f"media/{inv_pur_item.id}_{customer.name}_{total_price}.pdf"
                inv_pur_item.save()
                # Generating Invoice
                gen_pdf = GenereatePdf()
                gen_pdf.create_inv(
                    file_name=exact_file_name,
                    cus_name=customer.name,
                    cus_num=customer.phone_num,
                    cus_add=customer.address,
                    invoice_id=inv_pur_item.id,
                    prd_list=all_prod_list,
                    total_price=total_price)
                return response.Response({"success":"Invoice has been generated."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"No active PurchasedItem."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"No such customer exists."}, status=status.HTTP_400_BAD_REQUEST)

# Checked 
class InvoicePurchaseItemDeleteView(APIView):
    """DELETE - Delete InvoicePurchaseItem by their id."""
    def delete(self, request, pk, format=None):
        inv_purchase_item = InvoicePurchaseItem.objects.filter(id=pk)
        if len(inv_purchase_item)>0:
            inv_purchase_item = inv_purchase_item[0]
            inv_purchase_item.delete()
            return response.Response({"success":"Invoice has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid PurchaseItem."}, status=status.HTTP_400_BAD_REQUEST)
