from wsgiref.validate import validator
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle

from orders.models import *
from products.models import *
from orders.api.serializers import OrderSerializer, AdminOrderSerializer
from orders.api.permissions import IsOrderOwnerOrReadOnly
from orders.api.throttling import OrderCreateThrottle
from orders.api.paginations import OrderPagination


class OrderListView(generics.ListAPIView):
    # queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=OrderPagination
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        this_user=self.request.user
        return Order.objects.filter(customer=this_user)
    
class OrderCreateView(generics.CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    throttle_classes=[OrderCreateThrottle]
    
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        if not Product.objects.filter(id=pk).exists():
            raise ValidationError("No such product exists")
        this_product=Product.objects.get(id=pk)
        this_user=self.request.user
        serializer.save(product=this_product, customer=this_user)
        
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset=Order.objects.all()
    #serializer_class=OrderSerializer
    permission_classes=[IsOrderOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminOrderSerializer
        return OrderSerializer
    
    def perform_update(self, serializer):
        pk=self.kwargs.get("pk")
        
        if not Order.objects.filter(id=pk).exists():
            raise ValidationError("No such order exists")
        
        if self.request.user.is_staff:
            this_order=Order.objects.get(id=pk)
            
            this_product=this_order.product
            this_user=this_order.customer
            this_quantity=this_order.quantity
            this_order_placed=this_order.order_placed
            
            serializer.save(product=this_product, customer=this_user, quantity=this_quantity, order_placed=this_order_placed)
        else:
            this_order=Order.objects.get(id=pk)
            
            if this_order.delivered is True:
                raise ValidationError("Product already delivered")
            
            this_product=this_order.product
            this_user=self.request.user
            
            serializer.save(product=this_product, customer=this_user)
            
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        this_user=self.request.user
        return Order.objects.filter(customer=this_user)
            
            
            