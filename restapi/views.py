from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, CartSerializer
from .models import Product, Category, Cart
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'List': 'api/product-list/',
            'Detail View': 'api/product-detail/<str:pk>/',
            'Create': 'api/product-create/',
            'Update': 'api/product-update/<str:pk>/',
            'Delete': 'api/product-delete/<str:pk>/',
            'Cart-list': 'api/cart-list/',
            'Cart-detail': 'api/cart-detail/<str:pk>/',
            'Category-list': 'api/category-list/',
            'Token': 'api/token/',
            'Token-refresh': 'api/token/refresh/'
        }
        return Response(api_urls)

class ProductListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        products = Product.objects.get(productID=pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)

class ProductCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ProductUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk):
        product = Product.objects.get(productID=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ProductDeleteView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk):
        product = Product.objects.get(productID=pk)
        product.delete()
        return Response("Item deleted")

class CategoryListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class CartListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

class CartDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        cart = Cart.objects.get(cartID=pk)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data)

