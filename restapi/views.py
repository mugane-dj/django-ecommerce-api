from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import Product, Category, Cart
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserRegisterView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'username', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        operation_description="""
        This endpoint is used to register a new user.
        """,
        responses={
            200: openapi.Response('Success', UserRegisterSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductListView(APIView):
    permission_classes = (IsAuthenticated, )

    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[access_token_param_config],
              operation_description="""
        This endpoint is used to retrieve a list of available products.
        """,
        responses={
            200: openapi.Response('Success', None),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    id_param_config = openapi.Parameter('id',
                                        openapi.IN_PATH,
                                        description="Product ID",
                                        type=openapi.TYPE_INTEGER)
    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[id_param_config, access_token_param_config],
              operation_description="""
        This endpoint is used to retrieve specified product.
        """,
        responses={
            200: openapi.Response('Success', ProductSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request, pk):
        products = Product.objects.get(productID=pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)


class ProductCreateView(APIView):
    permission_classes = (IsAuthenticated, )

    id_param_config = openapi.Parameter('id',
                                        openapi.IN_PATH,
                                        description="Product ID",
                                        type=openapi.TYPE_INTEGER)
    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[id_param_config, access_token_param_config],
              operation_description="""
        This endpoint is used to create a new product.
        """,
        responses={
            200: openapi.Response('Success', ProductSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ProductUpdateView(APIView):
    permission_classes = (IsAuthenticated, )

    id_param_config = openapi.Parameter('id',
                                        openapi.IN_PATH,
                                        description="Product ID",
                                        type=openapi.TYPE_INTEGER)
    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[id_param_config, access_token_param_config],
              operation_description="""
        This endpoint is used to update details a specified product.
        """,
        responses={
            200: openapi.Response('Success', ProductSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def post(self, request, pk):
        product = Product.objects.get(productID=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ProductDeleteView(APIView):
    permission_classes = (IsAuthenticated, )

    id_param_config = openapi.Parameter('id',
                                        openapi.IN_PATH,
                                        description="Product ID",
                                        type=openapi.TYPE_INTEGER)
    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[id_param_config, access_token_param_config], 
              operation_description="""
        This endpoint is used to delete a specified product.
        """,
        responses={
            200: openapi.Response('Success', ProductSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def delete(self, request, pk):
        product = Product.objects.get(productID=pk)
        product.delete()
        return Response("Item deleted")


class CategoryListView(APIView):
    permission_classes = (IsAuthenticated, )

    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[access_token_param_config],
          operation_description="""
        This endpoint is used to list all product categories.
        """,
        responses={
            200: openapi.Response('Success', None),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class CartListView(APIView):
    permission_classes = (IsAuthenticated, )

    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[access_token_param_config],
               operation_description="""
        This endpoint is used to list all carts created.
        """,
        responses={
            200: openapi.Response('Success', None),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)


class CartDetail(APIView):
    permission_classes = (IsAuthenticated, )

    id_param_config = openapi.Parameter('id',
                                        openapi.IN_PATH,
                                        description="Product ID",
                                        type=openapi.TYPE_INTEGER)
    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[access_token_param_config],
               operation_description="""
        This endpoint is used to retrieve details of a specified cart.
        """,
        responses={
            200: openapi.Response('Success', CartSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request, pk):
        cart = Cart.objects.get(cartID=pk)
        serializer = CartSerializer(cart, many=False)
        return Response(serializer.data)
