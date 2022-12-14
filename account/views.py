from django.http import Http404
from rest_framework import status

from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from product.models import Product
from product.serializers import ProductSerializer, CategorySerializer
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
from .serializers import AccountSerializers
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import Account
from .permissions import AnonPermissionOnly
from .serializers import UserSerializers, RegisterCerializer
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,

)
from django.core.paginator import Paginator


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterCerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

    def get(self, request):

         user = User.objects.all()
         paginator = Paginator(user, 5)
         page_num = self.request.query_params.get('page')
         print(page_num)
         serializers = UserSerializers(paginator.page(page_num), many=True)
         return Response(serializers.data)


class UserDetailApiView(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404


    def get(self, request, id):
        user = self.get_object(id)
        serializers = UserSerializers(user)
        data = serializers.data
        return Response(data)


class UserDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserCount(APIView):
    def get(self, request):
        users = User.objects.all()
        count = len(users)
        data = {
            "user_count": count
        }
        return Response(data)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializers

    def post(self, request):
        serializers = AccountSerializers(data=request.data)
        if serializers.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email']
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                phone_number=request.data['phone_number'],
            )
            account.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)