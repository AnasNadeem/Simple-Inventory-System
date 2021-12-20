from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone_num = models.CharField(max_length=10)
    address = models.TextField()

class PurchaseItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)

class InvoicePurchaseItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_item = models.ManyToManyField(PurchaseItem)
    invoice = models.FileField(upload_to='', blank=True, null=True)

    