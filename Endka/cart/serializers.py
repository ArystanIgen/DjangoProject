from rest_framework import serializers
from .models import *
from auth_.serializers import UserSerializer
from service.serializers import *


class CartSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = (
            'id', 'customer', 'created_at', 'updated_at'
        )

class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = (
            'id', 'cart', 'item', 'quantity'
        )