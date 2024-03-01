from django.db import models

# Create your models here.
class Ads(models.Model):
    name=models.CharField(max_length=200,unique=True)
    banner=models.ImageField(upload_to='ads',blank=True)
    banner_2=models.ImageField(upload_to='ads',blank=True)
    banner_3=models.ImageField(upload_to='ads',blank=True)
    banner_4=models.ImageField(upload_to='ads',blank=True)
    banner_5=models.ImageField(upload_to='ads',blank=True)
    banner_6=models.ImageField(upload_to='ads',blank=True)
    desc=models.TextField(blank=True)
    desc_2=models.TextField(blank=True)
    desc_3=models.TextField(blank=True)
    desc_4=models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='Ads'
        verbose_name_plural='Ads'
    def __str__(self) :
        return self.name
    
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
    design_2image=models.ImageField(upload_to='products',blank=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    price_1kg=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    price_2kg=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    design_2price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
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