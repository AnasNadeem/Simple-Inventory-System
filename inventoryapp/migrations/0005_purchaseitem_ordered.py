# Generated by Django 4.0 on 2021-12-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0004_alter_invoicepurchaseitem_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
