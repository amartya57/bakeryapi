from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="orders")
    quantity=models.PositiveIntegerField()
    order_placed=models.DateTimeField(auto_now_add=True)
    delivered=models.BooleanField(default=False)
    
    def __str__(self):
        return self.customer.username + " | " + self.order_placed.strftime("%m/%d/%Y, %H:%M:%S")

