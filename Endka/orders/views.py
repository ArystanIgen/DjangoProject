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
from rest_framework import viewsets

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user)
        return queryset