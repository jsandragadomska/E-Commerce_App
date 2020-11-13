from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    #id = models.AutoField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    # null - django is not gonna make it required
    # blank - can be null into the database
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    amount = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=225, default='None')
    product_pic = models.ImageField(null=True, blank=True, upload_to="images/products/")

    def has_amount(self):
        return self.amount > 0
    

class Category(models.Model):
    name = models.CharField(max_length=225, default='None')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")