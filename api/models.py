# wardrobe/models.py
# from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=100,blank=True,null=True)


class UserProfile(models.Model):
    # username = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    username  = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    

class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='clothing_images/')
    owner = models.ForeignKey('auth.User', related_name='clothing_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=100)
    clothing_items = models.ManyToManyField(ClothingItem)
    owner = models.ForeignKey('auth.User', related_name='outfits', on_delete=models.CASCADE)

    def __str__(self):
        return self.name