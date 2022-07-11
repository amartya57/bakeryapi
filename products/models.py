from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    price=models.FloatField()
    launched=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="reviews")
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    description=models.CharField(max_length=200, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+" | "+self.product.name + " | " + self.review_user.username
