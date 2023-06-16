from django.db import models
from django.contrib.auth.models import User


class ShoppingCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShoppingItems(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(ShoppingCategory, on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=10, decimal_places=3)
    details = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.item_name


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_items = models.ManyToManyField(ShoppingItems, through='ShoppingCartItem')

    def __str__(self):
        return self.user.username


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    shopping_item = models.ForeignKey(ShoppingItems, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.shopping_item.item_name +" "+str(self.item_quantity)

