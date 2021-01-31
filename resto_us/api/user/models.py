from django.db import models
from django.contrib.auth.models import AbstractUser
from api.restraunt.models import restraunt

class resto_user(AbstractUser):
    name = models.CharField(max_length=50,default='Anonymous')
    email = models.EmailField(max_length=250,unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    phone=models.CharField(max_length=20,unique=True,default='0')
    user_type = models.CharField(max_length=1,default='A')
    photo=models.ImageField(null=True)
    restraunt_id = models.ForeignKey(restraunt,on_delete=models.CASCADE,null=True)

    session_token = models.CharField(max_length=10,default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


