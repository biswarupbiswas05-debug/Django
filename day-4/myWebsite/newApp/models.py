from django.db import models
from django.utils import  timezone

# Create your models here.
class Product (models.Model):
    PRODUCT_STATUS=(
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),
    )
    name = models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    created_at = models.DateTimeField(default= timezone.now)
    status = models.CharField(max_length=20, choices = PRODUCT_STATUS, default='available')
    
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    product_varieties = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.name
 
class ProductCertificate(models.Model):
    product=models.OneToOneField(Product, on_delete= models.CASCADE)
    certificate_number= models.CharField(max_length=100)
    certificate_date = models.DateField(default=timezone.now)

    def  __str__(self):
       return f"Certificate for {self.product.name}"