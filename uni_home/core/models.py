from distutils.command.upload import upload
from email.policy import default
from ftplib import MAXLINE
from operator import truediv
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ClearableFileInput, ModelForm,forms
from django import forms
# Create your models here.
User=get_user_model()


class Profile(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    id_user=models.IntegerField()
    seller_name=models.CharField(max_length=100, blank=True,null=True)
    seller=models.BooleanField(default=False)
    name_surname=models.CharField(max_length=100, blank=True,null=True)
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_images', default='blank_profile.jpg')
    location=models.CharField(max_length=100, blank=True)
    università=models.CharField(max_length=100, blank=True)
    phone_number=PhoneNumberField(max_length=15,default='')
    email=models.EmailField(max_length=50,blank=True)
    def __str__(self):
        return self.user.username



class Post(models.Model):
    
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100, default='')
    caption=models.TextField(max_length=50000)
    phone_number=PhoneNumberField(max_length=15,default='',blank=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)
    price=models.IntegerField()
    position=models.CharField(max_length=100, default='')
    num_max_pers=models.IntegerField(default=0)

    def __str__(self):
        return self.user
    


        




class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'post_images',default='blank_profile.jpg')

    def __str__(self):
        return self.post.user
    



    

   
