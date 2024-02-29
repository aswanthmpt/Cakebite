from django.db import models
from mainapp.models import Product

# Create your models here.
class Cart(models.Model):
    user=models.CharField(max_length=200)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        db_table='Cart'