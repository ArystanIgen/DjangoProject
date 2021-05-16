from django.urls import path,include
from rest_framework import routers
from orders import views



app_name = 'order'
urlpatterns = [
    path('create/', views.order, name='order_create'),
    path('detail/', views.order_detail)
]