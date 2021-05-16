from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import action
from rest_framework.response import Response
from service.models import Item
from .cart import Cart
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework import status
from .models import Cart,CartItem
from rest_framework import viewsets
import logging

logger = logging.getLogger(__name__)

class CartViewSet(viewsets.ModelViewSet):

    serializer_class = CartSerializer


    def get_queryset(self):
        a = self.request.user.profile
        return Cart.objects.filter(customer=a.id)

    @action(methods=['post', 'put'],detail=True)
    def add_to_cart(self, request, pk=None):
        cart = self.get_object()
        item = Item.objects.get(pk=request.data['item_id'])
        quantity = int(request.data['quantity'])

        cart_item = CartItem.objects.filter(cart=cart,item=item).first()
        if cart_item:
            cart_item.quantity += quantity
            logger.info(f"Quantity have been changed, ID: {cart_item.cart}")
            cart_item.save()
        else:
            new_cart_item = CartItem(cart=cart, item=item, quantity=quantity)
            logger.info(f"Created new cart item ID: {new_cart_item.cart}")
            new_cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(methods=['post', 'put'], detail=True)
    def remove_from_cart(self, request, pk=None):
        cart = self.get_object()
        item = Item.objects.get(pk=request.data['item_id'])

        cart_item = CartItem.objects.filter(cart=cart, item=item).first()
        if cart_item==1:
            logger.info(f"Deletion of cart item, ID: {cart_item.cart}")
            cart_item.delete()
        else:
            cart_item.quantity=-1
            logger.info(f"Reducing quantity, ID: {cart_item.cart}")
            cart_item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):

    serializer_class = CartItemSerializer


    def get_queryset(self):
        p = self.request.user.profile
        c=Cart.objects.get(customer=p)
        return CartItem.objects.filter(cart=c.id)