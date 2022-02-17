

from urllib import request
from django.shortcuts import render
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models





class CustomUser(AbstractUser):
    # instance = Balance(user = request.user, Balance = 0)
    # instance.save()
   
    pass
    # add additional fields in here
   

    def __str__(self):
        
        return self.username

class Balance(models.Model):
       user = models.ForeignKey(CustomUser,   on_delete=models.CASCADE, )
       balance = models.IntegerField(default = 0)



