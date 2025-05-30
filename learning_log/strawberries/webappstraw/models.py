from django.db import models


#товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.DecimalField(max_digits=20)
    image = models.ImageField()
    ball = models.BooleanField()
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    supplier = models.CharField(max_length=255)
    delivery_duration = models.DurationField()


#Поставщик
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=10)


#Пользователь
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=8)
    adress = models.CharField(max_length=100)
    id = models.DecimalField(max_digits=10)


#Заказ
class Order(models.Model):
    order_id = models.DecimalField(max_digits=10)
    amount = models.DecimalField(max_digits=2)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.DecimalField(max_digits=10)
    adress = models.CharField(max_length=100)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_duration = models.DurationField()

