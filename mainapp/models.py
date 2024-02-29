from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to='categoris',blank=True)
    image_2=models.ImageField(upload_to='categoris',blank=True)
    image_3=models.ImageField(upload_to='categoris',blank=True)
    banner=models.ImageField(upload_to='categoris',blank=True)
    desc=models.TextField(blank=True)
    desc_2=models.TextField(blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
        
    def __str__(self) :
        return self.name
class Subcategory(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to='categoris',blank=True)
    image_2=models.ImageField(upload_to='categoris',blank=True)
    image_3=models.ImageField(upload_to='categoris',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    banner=models.ImageField(upload_to='categoris',blank=True)
    desc=models.TextField(blank=True)
    desc_2=models.TextField(blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='subcategory'
        verbose_name_plural='subcategories'
        
    def __str__(self) :
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    category=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products',blank=True)
    image_2=models.ImageField(upload_to='products',blank=True)
    image_3=models.ImageField(upload_to='products',blank=True)
    image_4=models.ImageField(upload_to='products',blank=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    flavour=models.CharField(max_length=250,blank=True)
    type=models.CharField(max_length=250,blank=True)
    shape=models.CharField(max_length=250,blank=True)
    weight=models.FloatField(blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return self.name