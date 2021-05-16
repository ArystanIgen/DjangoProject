from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import action
from rest_framework.response import Response
from service.models import Item
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action, api_view, permission_classes, parser_classes
from .serializers import *
from rest_framework import status
from service.permissions import BusinessOrAdminPermission
from cart.models import CartItem
from .models import Order
import logging

logger = logging.getLogger(__name__)



@api_view(['POST'])
def order(request):
    if request.method=='POST':
        total=0
        user=request.user
        profile=user.profile
        cart=profile.carts
        cart_items=CartItem.objects.filter(cart=cart)
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            order=serializer.save()
            for i in cart_items:
                p=i.item
                OrderItem.objects.create(
                    order=order,
                    item=i.item,
                    price=p.price,
                    quantity=i.quantity
                )
                total+=float(p.price)
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Serializer is not valid, errors: {serializer.errors}")
        return Response({'error': 'error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((BusinessOrAdminPermission,))
def order_detail(request):
    if request.method == 'GET':
        profile=request.user.profile
        queryset = OrderItem.objects.filter(owner=profile)
        serializer = OrderItemSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)