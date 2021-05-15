from rest_framework import serializers
from .models import *
from auth_.serializers import UserSerializer




class ItemSerializer(serializers.ModelSerializer):
    owner= UserSerializer(read_only=True)
    class Meta:
        model = Item
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields="__all__"

