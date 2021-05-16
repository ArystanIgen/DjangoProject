from rest_framework import serializers
from .models import *
from auth_.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'adress', 'city','country'
        )

class OrderItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderItem
        fields = "__all__"