from rest_framework.serializers import ModelSerializer
from inventoryapp.models import Item, PurchaseItem, InvoicePurchaseItem, Customer

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class PurchaseItemViewSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer).data
        response['item'] = ItemSerializer(instance.item).data
        return response

class PurchaseItemSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"