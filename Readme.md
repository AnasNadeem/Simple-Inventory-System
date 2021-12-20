# Inventory System

Its a simple inventory system where you can create items, purchase it and create invoice of it.

## Endpoints:

### Item urls 
``` 
path('list-item/', ItemListView.as_view()),
path('create-item/', ItemCreateView.as_view()),
path('update-item/<int:pk>/', ItemUpdateView.as_view()),
path('delete-item/<int:pk>/', ItemDeleteView.as_view()),
```
### Customer urls 
```
path('list-customer/', CustomerListView.as_view()),
path('create-customer/', CustomerCreateView.as_view()),
path('update-customer/<int:pk>/', CustomerUpdateView.as_view()),
path('delete-customer/<int:pk>/', CustomerDeleteView.as_view())
```
### Purchase item urls
```
path('list-puritem/', PurchaseItemListView.as_view()),
path('list-orderedpuritem/', PurchaseItemOrderedListView.as_view()),
path('list-unorderedpuritem/', PurchaseItemUnOrderedListView.as_view()),
path('list-puritem/<customer>/', PurchaseItemCustomerListView.as_view()),
path('create-puritem/', PurchaseItemCreateView.as_view()),
path('update-puritem/<int:pk>/', PurchaseItemUpdateView.as_view()),
path('delete-puritem/<int:pk>/', PurchaseItemDeleteView.as_view())
```
### Invoice purchase item urls
```
path('list-invpuritem/', InvoicePurchaseItemListView.as_view()),
path('create-invpuritem/', InvoicePurchaseItemCreateView.as_view()),
# path('delete-invpuritem/<int:pk>/', InvoicePurchaseItemDeleteView.as_view()),
path('get-invoice/<int:pk>/', InvoicePurchaseItemView.as_view()) 
```

### How to run this project:
### Prequisite
* You should have Python installed on your Machine.
Now Open Terminal or Shell.

### Steps:
1. ``` python -m pip install requirements.txt ```
2. ``` python manage.py runserver ```

## Enjoy :)