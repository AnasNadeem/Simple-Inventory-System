# Generated by Django 4.0 on 2021-12-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0003_alter_invoicepurchaseitem_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicepurchaseitem',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
