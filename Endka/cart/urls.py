from django.urls import path,include
from rest_framework import routers
from cart import views

router = routers.DefaultRouter()
router.register(r'carts', views.CartViewSet,basename='cart')
router.register(r'cart_items', views.CartItemViewSet,basename='cart_items')

app_name = 'cart'
urlpatterns = [
    path('', include(router.urls)),
]