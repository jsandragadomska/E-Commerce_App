from django.db import models

# Create your models here.
class Product(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length=255)
    # null - django is not gonna make it required
    # blank - can be null into the database
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    amount = models.IntegerField(null=True, blank=True)
