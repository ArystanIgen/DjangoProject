from django.urls import path,include
from rest_framework import routers
from order import views


router = routers.DefaultRouter()
router.register(r'orders', views.CartViewSet,basename='order')


app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
]