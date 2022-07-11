from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import filters

from products.models import *
from products.api.serializers import ReviewSerializer, ProductSerializer
from products.api.permissions import IsAdminOrReadOnly, IsReviewOwnerOrReadOnly
from products.api.paginations import ProductListPagination

class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(product=pk)
    
class ReviewCreate(generics.CreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        this_product=Product.objects.get(id=pk)
        
        this_user=self.request.user
        review_query=Review.objects.filter(product=this_product, review_user=this_user)
        
        if review_query.exists():
            raise ValidationError("You have already reviewed this product")
        
        serializer.save(product=this_product, review_user=this_user)
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        pk=self.kwargs.get("pk")
        this_review=Review.objects.get(id=pk)
        this_product=this_review.product
        this_user=self.request.user
        
        serializer.save(product=this_product, review_user=this_user)
        
class ProductListAV(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAdminOrReadOnly]
    pagination_class=ProductListPagination
    filter_backends=[filters.OrderingFilter, filters.SearchFilter]
    search_fields=['name', 'description']
    ordering_fields=['price']
    
class ProductDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAdminOrReadOnly, IsAuthenticated]