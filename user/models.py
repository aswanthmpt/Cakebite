from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.CharField(max_length=222)
    auth=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    pincode=models.IntegerField()
    mobileno=models.IntegerField()
    image=models.ImageField(upload_to='userimg')
    
    def __str__(self):
        return self.user