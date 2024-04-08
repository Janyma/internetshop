from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
