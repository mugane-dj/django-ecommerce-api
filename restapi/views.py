from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle


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
    
    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    
    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def get(self, request, *args, **kwargs):
        productID = kwargs['pk']
        if cache.get(productID):
            product = cache.get(productID)
            print("Cache hit")
        else: 
            try:
                product = Product.objects.get(pk=productID)
                cache.set(productID, product)
                print("Cache miss")
            except Product.DoesNotExist:
                return Response(status=404)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


class ProductCreateView(APIView):
    
    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ProductUpdateView(APIView):

    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def post(self, request, *args, **kwargs):
        productID = kwargs['pk']

        if cache.get(productID):
            product = cache.get(productID)
            print("Cache hit")
        else:
            try:
                product = Product.objects.get(pk=productID)
                cache.set(productID, product)
                print("Cache miss")
            except Product.DoesNotExist:
                return Response(status=404)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ProductDeleteView(APIView):

    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })
        
    def delete(self, request, *args, **kwargs):
        productID = kwargs['pk']
        if cache.get(productID):
            product = cache.get(productID)
            print("Cache hit")
        else:
            try:
                product = Product.objects.get(pk=productID)
                cache.set(productID, product)
                print("Cache miss")
            except Product.DoesNotExist:
                return Response(status=404)
        product.delete()
        return Response("Item deleted")


class CategoryListView(APIView):

    throttle_classes = [UserRateThrottle]
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
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class OrderListView(APIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = (IsAuthenticated, )

    access_token_param_config = openapi.Parameter('Authorization',
                                                  openapi.IN_HEADER,
                                                  description="access token",
                                                  type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[access_token_param_config],
               operation_description="""
        This endpoint is used to retrieve a list of all placed orders.
        """,
        responses={
            200: openapi.Response('Success', None),
            400: openapi.Response('Bad Request', None),
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):

    throttle_classes = [UserRateThrottle]
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
        This endpoint is used to retrieve details of a specified order item.
        """,
        responses={
            200: openapi.Response('Success', OrderSerializer),
            400: openapi.Response('Bad Request', None),
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def get(self, request, *args, **kwargs):
        orderItemID = kwargs['pk']
        if cache.get(orderItemID):
            order = cache.get(orderItemID)
            print("Cache hit")
        else:
            try:
                order = OrderItem.objects.get(pk=orderItemID)
                cache.set(orderItemID, order)
                print("Cache miss")
            except Order.DoesNotExist:
                return Response(status=404)
        serializer = OrderItemSerializer(order, many=False)
        return Response(serializer.data)

class AddressDetailView(APIView):
    
    throttle_classes = [UserRateThrottle]
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
        This endpoint is used to retrieve a specified shipping address.
        """,
        responses={
            200: openapi.Response('Success', ShippingAddressSerializer),
            400: openapi.Response('Bad Request', None),
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def get(self, request, *args, **kwargs):
        addressID = kwargs['pk']
        if cache.get(addressID):
            address = cache.get(addressID)
            print("Cache hit")
        else: 
            try:
                address = ShippingAddress.objects.get(pk=addressID)
                cache.set(addressID, address)
                print("Cache miss")
            except ShippingAddress.DoesNotExist:
                return Response(status=404)
        serializer = ShippingAddressSerializer(address, many=False)
        return Response(serializer.data)


class AddressCreateView(APIView):
    
    throttle_classes = [UserRateThrottle]
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['address', 'country', 'city', 'state', 'zipcode', 'phone'],
            properties={
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'country': openapi.Schema(type=openapi.TYPE_STRING),
                'city': openapi.Schema(type=openapi.TYPE_STRING),
                'state': openapi.Schema(type=openapi.TYPE_STRING),
                'zipcode': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        operation_description="""
        This endpoint is used to create a new shipping address.
        """,
        responses={
            200: openapi.Response('Success', ShippingAddressSerializer),
            400: openapi.Response('Bad Request', None),
            500: openapi.Response('Internal Server Error', None),
        })
    def post(self, request):
        serializer = ShippingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class AddressUpdateView(APIView):

    throttle_classes = [UserRateThrottle]
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
        This endpoint is used to update details of a specified shipping address.
        """,
        responses={
            200: openapi.Response('Success', ShippingAddressSerializer),
            400: openapi.Response('Bad Request', None),
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })

    def post(self, request, *args, **kwargs):
        addressID = kwargs['pk']
        if cache.get(addressID):
            address = cache.get(addressID)
            print("Cache hit")
        else: 
            try:
                address = ShippingAddress.objects.get(pk=addressID)
                cache.set(addressID, address)
                print("Cache miss")
            except ShippingAddress.DoesNotExist:
                return Response(status=404)
        serializer = ShippingAddressSerializer(instance=address, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

 
       
class AddressDeleteView(APIView):

    throttle_classes = [UserRateThrottle]
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
        This endpoint is used to delete a specified shipping address.
        """,
        responses={
            200: openapi.Response('Success', ShippingAddressSerializer),
            400: openapi.Response('Bad Request', None),
            404: openapi.Response('Not Found', None),
            500: openapi.Response('Internal Server Error', None),
        })
    
    def delete(self, request, *args, **kwargs):
        addressID = kwargs['pk']
        if cache.get(addressID):
            address = cache.get(addressID)
            print("Cache hit")
        else: 
            try:
                address = ShippingAddress.objects.get(pk=addressID)
                cache.set(addressID, address)
                print("Cache miss")
            except ShippingAddress.DoesNotExist:
                return Response(status=404)
        address.delete()
        return Response("Item deleted")


class ReviewDetailView(APIView):
    
        throttle_classes = [UserRateThrottle]
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
            This endpoint is used to retrieve a specified review.
            """,
            responses={
                200: openapi.Response('Success', ProductReviewSerializer),
                400: openapi.Response('Bad Request', None),
                404: openapi.Response('Not Found', None),
                500: openapi.Response('Internal Server Error', None),
            })
    
        def get(self, request, *args, **kwargs):
            ReviewID = kwargs['pk']
            if cache.get(ReviewID):
                review = cache.get(ReviewID)
                print("Cache hit")
            else: 
                try:
                    review = ProductReview.objects.get(pk=ReviewID)
                    cache.set(ReviewID, review)
                    print("Cache miss")
                except ProductReview.DoesNotExist:
                    return Response(status=404)
            serializer = ProductReviewSerializer(review, many=False)
            return Response(serializer.data)

class ReviewCreateView(APIView):
    
        throttle_classes = [UserRateThrottle]
        permission_classes = (IsAuthenticated, )
    
        @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                required=['review', 'rating'],
                properties={
                    'review': openapi.Schema(type=openapi.TYPE_STRING),
                    'rating': openapi.Schema(type=openapi.TYPE_INTEGER),
                },
            ),
            operation_description="""
            This endpoint is used to create a new product review.
            """,
            responses={
                200: openapi.Response('Success', ProductReviewSerializer),
                400: openapi.Response('Bad Request', None),
                500: openapi.Response('Internal Server Error', None),
            })

        def post(self, request):
            serializer = ProductReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

class ReviewDeleteView(APIView):
    
        throttle_classes = [UserRateThrottle]
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
            This endpoint is used to delete a specified review.
            """,
            responses={
                200: openapi.Response('Success', ProductReviewSerializer),
                400: openapi.Response('Bad Request', None),
                404: openapi.Response('Not Found', None),
                500: openapi.Response('Internal Server Error', None),
            })
        def delete(self, request, *args, **kwargs):
            ReviewID = kwargs['pk']
            if cache.get(ReviewID):
                review = cache.get(ReviewID)
                print("Cache hit")
            else: 
                try:
                    review = ProductReview.objects.get(pk=ReviewID)
                    cache.set(ReviewID, review)
                    print("Cache miss")
                except ProductReview.DoesNotExist:
                    return Response(status=404)
            review.delete()
            return Response("Item deleted")