from django.urls import path,include
from service.views import RestaurantViewSet, ItemViewset
from rest_framework.routers import DefaultRouter

app_name = 'service'
router = DefaultRouter()

router.register('restaurants', RestaurantViewSet, basename='service')
router.register('items', ItemViewset, basename='service')
urlpatterns = [
    path('', include(router.urls)),
]
