import requests
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import generics
from rest_framework import mixins
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

from .models import Vendor, Product
from .serializers import VendorSerializer, ProductSerializer


class ApiOverview(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            'name': 'John',
            'age': 19
        }
        return Response(data)


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    template_name = 'user_home.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return "HSHH"




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.pk

        try:
            context["token"] = Token.objects.get(user_id=user_id).key
        except:
            context["token"] = None
        context["user"] = User.objects.get(id=user_id)
        return context




class VendorsView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

    def get(self, request, *args, **kwargs):
        print(request.user)
        return self.list(self, request, *args, **kwargs)


class ProductsView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class ProductsByTypeView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    # queryset = Product.objects.filter(product_type=type)

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(product_type=self.kwargs.get('type'))

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, *kwargs)


class ProductsByPkView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    # queryset = Product.objects.filter(product_type=type)

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, *kwargs)


class ProductByVendorPkView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    # queryset = Product.objects.filter(product_type=type)

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(product_vendor_id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, *kwargs)
