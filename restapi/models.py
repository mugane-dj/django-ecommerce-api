from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

class Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    cartID = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0)
    total = MoneyField(max_digits=14, decimal_places=2, default_currency='KSH')

    def __str__(self):
        return self.cartID
