from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
app_name = 'auth'
urlpatterns = [
    path('login/', obtain_jwt_token)
]