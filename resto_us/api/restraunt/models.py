from django.db import models
import random

def generate_code(length=6):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(65,91)] + [str(i) for i in range(10)]) for _ in range(length))


class restraunt(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(null=True,blank=True)
    about = models.TextField()
    latitude = models.CharField(max_length=50,null=True,blank=True)
    longitude = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True)
    rating = models.PositiveIntegerField(default=0)
    open_time = models.CharField(max_length=50,null=True,blank=True)
    close_time = models.CharField(max_length=50,null=True,blank=True)
    rest_code = models.CharField(max_length=10,default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class restraunt_standards(models.Model):
    restraunt_id = models.ForeignKey(restraunt,on_delete=models.CASCADE)
    deal_title = models.CharField(max_length=50,null=True,blank=True)
    deal_description = models.TextField(null=True,blank=True)
    deal_banner = models.ImageField(null=True)
    no_of_meals = models.PositiveIntegerField(default=0)
    value_of_meal = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    min_days = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
