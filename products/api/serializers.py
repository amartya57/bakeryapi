from itertools import product
from django.db.models import Sum
from rest_framework import serializers
from products.models import *

class ReviewSerializer(serializers.ModelSerializer):
    
    review_user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Review
        # fields="__all__"
        exclude=['product', 'created', 'update']

class ProductSerializer(serializers.ModelSerializer):
    
    # reviews=ReviewSerializer(many=True, read_only=True)
    
    num_ratings=serializers.SerializerMethodField(read_only = True)
    average_rating=serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model=Product
        fields="__all__"

    def get_num_ratings(self, object):
        return object.reviews.count()
    
    def get_average_rating(self, object):
        num_ratings = self.get_num_ratings(object)
        if num_ratings==0:
            return 0
        # total=0
        # for review in object.reviews.all():
        #     total+=review.rating
        review_query=Review.objects.filter(product=object)
        total=review_query.aggregate(Sum('rating'))['rating__sum']
        return total/num_ratings