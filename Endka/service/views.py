from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import RestaurantSerializer,ItemSerializer
from .search import DynamicSearchFilter
from rest_framework.parsers import MultiPartParser
from .permissions import BusinessOrAdminPermission


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    parser_classes = [MultiPartParser]

    filter_backends = (DynamicSearchFilter,)
    permission_classes = (BusinessOrAdminPermission,)




class ItemViewset(viewsets.ModelViewSet):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    filter_backends = (DynamicSearchFilter,)
    parser_classes = [MultiPartParser]
    permission_classes = (BusinessOrAdminPermission,)