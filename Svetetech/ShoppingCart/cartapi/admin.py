from django.contrib import admin
from .models import ShoppingItems, ShoppingCategory, ShoppingCartItem, ShoppingCart

admin.site.register(ShoppingItems)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(ShoppingCategory)
# Register your models here.
