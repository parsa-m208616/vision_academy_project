from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import ProductSerializer, FileSerializer, CategorySerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'erorr': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):

        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'erorr': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)

class FileListView(APIView):
    def get(self, request, product_pk):
        try:
            # files = Product.objects.get(pk=product_pk).file_set.all()
            files = File.objects.filter(product__id=product_pk)

        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, pk, product_pk):
        try:
            file = File.objects.get(pk=pk, product_pk=product_pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data)
