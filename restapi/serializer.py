from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'