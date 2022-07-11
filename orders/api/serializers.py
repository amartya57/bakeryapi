from itertools import product
from django.db.models import Sum
from rest_framework import serializers
from orders.models import *

class OrderSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    
    price=serializers.SerializerMethodField()
    order_value=serializers.SerializerMethodField()
    
    class Meta:
        model=Order
        fields="__all__"
        
    def get_order_value(self, object):
        return (object.quantity * object.product.price)
    
    def get_price(self, object):
        return object.product.price
    
class AdminOrderSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    
    price=serializers.SerializerMethodField()
    order_value=serializers.SerializerMethodField()
    
    class Meta:
        model=Order
        fields="__all__"
        extra_kwargs={
            'customer':{
                'read_only':True
            },
            'product':{
                'read_only':True
            },
            'quantity':{
                'read_only':True
            },
            'order_placed':{
                'read_only':True
            },
        }
        
    def get_order_value(self, object):
        return (object.quantity * object.product.price)
    
    def get_price(self, object):
        return object.product.price