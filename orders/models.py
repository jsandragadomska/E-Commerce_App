from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

# Create your models here.
User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    # refactor shipping addres to its own model
    shipping_address = models.TextField(blank=True, null=True)
