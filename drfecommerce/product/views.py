from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer, tags=["Category"])
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing brands
    """

    queryset = Brand.objects.all()
    name = "Brand"

    @extend_schema(responses=BrandSerializer, tags=["Brand"])
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer, tags=["Product"])
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
