from _ast import Or

from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import generics, permissions
# from rest_framework.permissions import OR


from ..permission import IsSuperUser, IsUser, IsAdmin
from .serializers import *
from ..models import *


from ..models import ShoppingCart, ShoppingCartItem
from .serializers import CartItemSerializer


class ShoppingCartItemAPIView(generics.ListCreateAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsUser, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart = ShoppingCart.objects.get(user=self.request.user)
        item = serializer.validated_data['item']
        quantity = serializer.validated_data.get('quantity', 1)
        existing_cart_item = ShoppingCart.objects.filter(cart=cart, item=item).first()
        if existing_cart_item:
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            serializer.save(cart=cart, quantity=quantity)


class ShoppingCartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
