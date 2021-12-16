from rest_framework.serializers import ModelSerializer
from inventoryapp.models import Item, PurchaseItem, InvoicePurchaseItem

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PurchaseItemSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['item'] = ItemSerializer(instance.item).data
    #     return response
