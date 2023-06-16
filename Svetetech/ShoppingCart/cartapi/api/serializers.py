from rest_framework import serializers
from ..models import ShoppingCartItem, ShoppingItems, ShoppingCart, ShoppingCategory


class ShoppingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCategory
        fields = '__all__'


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItems
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    item = ShoppingItemSerializer()

    class Meta:
        model = ShoppingCartItem
        fields = '__all__'