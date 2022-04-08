from ast import Or
from lib2to3.pgen2 import token
from django.db import models
from product.models import Product


class Order(models.Model):
    token = models.CharField(
        max_length=250,
        blank=True
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='TL Sipariş Toplamı'
    )
    emailAddress = models.EmailField(
        max_length=250,
        blank=True,
        verbose_name='E-mail'
    )
    created = models.DateField(
        auto_now_add=True
    )
    billingName = models.CharField(
        max_length=250,
        blank=True
    )
    billingAddress1 = models.CharField(
        max_length=250,
        blank=True
    )
    billingCity = models.CharField(
        max_length=250,
        blank=True
    )
    billingPostCode = models.CharField(
        max_length=10,
        blank=True
    )
    billingCountry = models.CharField(
        max_length=200,
        blank=True
    )
    shippingName = models.CharField(
        max_length=250,
        blank=True
    )
    shippingAddress1 = models.CharField(
        max_length=250,
        blank=True
    )
    shippingCity = models.CharField(
        max_length=250,
        blank=True
    )
    shippingPostCode = models.CharField(
        max_length=10,
        blank=True
    )
    shippingCountry = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        db_table = 'order'
        ordering = ('-created',)

    def __str__(self):
        return "{}".format(self.id)





class OrderItem(models.Model):
    product = models.CharField(
        max_length=250,
        blank=True
    )
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='TL Tutar'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'OrderItem'

    def sub_totaL(self):
        return self.quantity * self.price

    def __str__(self):
        return "{}".format(self.product)





class Cart(models.Model):
    cart_id = models.CharField(
        max_length=250,
        blank=True
    )
    date_added = models.DateField(
        auto_now_add=True
    )
    class Meta:
        db_table='Cart'
        ordering = ['date_added',]

    def __str__(self):
        return "{}".format(self.cart_id)





class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    active = models.BooleanField(
        default = True
    )
    class Meta:
        db_table = 'CartItem'
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return "{}".format(self.product)





