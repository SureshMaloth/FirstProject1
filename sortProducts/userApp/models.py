from django.db import models
from django.core.validators import MaxValueValidator
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category=models.CharField(max_length=100,default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
    
class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.0)])
    date=models.DateField()
    
    def __str__(self):
        return self.user
