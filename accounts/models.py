from logging import PlaceHolder
from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver


# Model to store user profiles.
class UserName_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Email_Id = models.EmailField(max_length=100, null =True, blank=True, unique=True)
    name = models.CharField(max_length=200,null=True, blank = True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(default = 'accounts/profile_pics/images/profile1.png',upload_to='accounts/profile_pics/images/',null =True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return str(self.name)


# Model to store recipes.
class Recipes(models.Model):
    
    Recipe_name = models.CharField(max_length=100, null=True)
    
    CATEGORY = (
        ('North Indian','North Indian'),
        ('South Indian','South Indian'),
        ('Italian','Italian'),
        ('Healthy Salad','Healthy Salad'),
        ('Bakery','Bakery'),
        # ('Non veg')
    )
    
    user = models.ForeignKey(UserName_Profile, on_delete=models.CASCADE,related_name='food')
    Recipe_Type = models.CharField(max_length=100, null = True, choices=CATEGORY)
    Recipe_Owner = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    Image = models.ImageField(upload_to='accounts/Food_pics/images/',null =True, blank = True)
    description = models.TextField(max_length=2000,null=True,blank=True)
    ingredients = models.TextField(max_length=1000,null=True,blank=True)
    servings = models.CharField(max_length=5,null=True,blank=True)
    time = models.CharField(max_length=5,null=True,blank=True)
    calories = models.CharField(max_length=5,null=True,blank=True)
    Steps = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.Recipe_name

 # Model to store user reviews/comments on recipes.   
class review(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=80,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    recipes2 = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return "%s" %(self.recipes2.Recipe_name)
    


# Model to store user contact messages.
class Contact(models.Model):
    username = models.CharField(max_length=200,null=True, blank = True)

    email = models.EmailField(max_length=100, null =True, blank=True)
    
    Issue = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.email





