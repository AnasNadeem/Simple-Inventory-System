from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class PurchaseItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class InvoicePurchaseItem(models.Model):
    purchase_item = models.ForeignKey(PurchaseItem, on_delete=models.CASCADE)
    invoice = models.FileField(upload_to='invoice/')

    