from rest_framework import serializers
from .models import *
from auth_.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):

    customer = UserSerializer(read_only=True)


    class Meta:
        model = Order
        fields = (
            'id', 'customer', 'total', 'created_at', 'updated_at'
        )



class OrderItemSerializer(serializers.ModelSerializer):


    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            'id', 'order', 'product', 'quantity'
        )