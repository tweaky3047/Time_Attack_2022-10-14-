from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    
    phone_number= models.CharField(max_length=256, default='')
    address = models.CharField(max_length=256, default='')