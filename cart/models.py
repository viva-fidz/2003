from django.db import models


# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    item = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    item_total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)