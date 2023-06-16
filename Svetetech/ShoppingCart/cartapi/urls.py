from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from .api.views import ShoppingCartItemAPIView, ShoppingCartItemDetailAPIView

urlpatterns = [
    # path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/cart-items/', ShoppingCartItemAPIView.as_view(), name='cart-items'),
    path('api/cart-items/<int:pk>/', ShoppingCartItemDetailAPIView.as_view(), name='cart-item-detail'),
]
