from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import UpdateAPIView,RetrieveAPIView
from .serializers import RegistrationSerializer,ChangePasswordSerializer,UpdateUserSerializer,UserSerializer
from .models import UserNew,Profile

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self,request):
        user=request.data.get('user',{})

        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangePasswordAPIView(UpdateAPIView):

    queryset = UserNew.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    def get(self,request,pk,*args, **kwargs):
        profile=UserNew.objects.get(pk=pk)
        if request.user.profile.pk!= profile.pk:
            return Response(status=status.HTTP_423_LOCKED)
        return self.retrieve(request, *args, **kwargs)