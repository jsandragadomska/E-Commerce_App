from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save
from datetime import datetime, date

from products.models import Product

# Create your models here.
User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('Shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created')
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    # refactor shipping addres to its own model
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def calculate(self, save=False):
        if not self.product:
            return{}
        sub_total = self.product.price
        tax_rate = 0.30
        tax_total = sub_total * tax_rate
        tax_total = float("%.2f" %(tax_total))
        total = sub_total + tax_total
        total = float("%.2f" %(total))
        totals = {
            "subtotal": sub_total,
            "tax": tax_total,
            "total": total
        }
        for k,v in totals.items():
            setattr(self, k, v)
            if save == True:
                self.save()
        
        return totals
    
def order_pre_save(sender, instance, *args, **kwargs):
    instance.calculate(save=False)

pre_save.connect(order_pre_save, sender=Order)

def order_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.calculate(save=True)

post_save.connect(order_post_save, sender=Order)