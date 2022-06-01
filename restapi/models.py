from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name
class OrderStatus(models.Model):
    order_status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.order_status_name
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = MoneyField(max_digits=14, decimal_places=2, default_currency='KSH')
    stock = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.product_name

class ProductReview(models.Model):
    reviewID = models.CharField(max_length=100, primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review
class Order(models.Model):
    orderID = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.orderID

    @property
    def cart_total(self):
       orderitems = self.orderitem_set.all()
       total = sum([item.get_total for item in orderitems])
       return total

    @property
    def cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping_order(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if item.OrderStatus.order_status_name == "processed":
                shipping = True
        return shipping

class OrderItem(models.Model):
    orderItemID = models.CharField(max_length=100, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.product_name

    @property
    def get_total(self):
        total = self.quantity * self.product.product_price
        return total

class ShippingAddress(models.Model):
    addressID = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)
    phone_number = PhoneNumberField(null=False)
    country = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addressID
