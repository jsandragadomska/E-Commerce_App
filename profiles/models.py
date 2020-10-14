from django.db import models

# Create your models here.
class Profile(models.Model):
    #id = models.AutoField()
    login = models.CharField(max_length=255)
    content = models.TextField()
    # firstname
    # lastname
    # image
    # address