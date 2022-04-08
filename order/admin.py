from ast import Or
from django.contrib import admin
from .models import Order,OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product',{'fields':['product'],}),
        ('Quantity',{'fields':['quantity'],},
        ('Price',{'fields':['price'],}),)

    ]
    readonly_fields = ['product','quantity', 'price']
    can_delete=False
    max_num =0



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','emailAddress', 'created']
    list_display_links = ('id','billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    
