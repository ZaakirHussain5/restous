from django.db import models

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class restraunt_standards(models.Model):
    restraunt_id = models.OneToOneField(restraunt,on_delete=models.CASCADE)
    no_of_meals = models.PositiveIntegerField(default=0)
    value_of_meal = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    min_days = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
