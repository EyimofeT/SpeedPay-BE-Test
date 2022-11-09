
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# from . import helpers
# Create your models here.

# class User(models.Model):


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    title = None
    balance = models.FloatField(default=0.0)
    account_number= models.IntegerField( unique = True)
    # balance = 0
    # account_number = helpers.generate_account_number()
    # last_login = models.CharField(default=datetime.datetime.now(),max_length=200)
    # completed = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.title


class Deposit(models.Model):
    amount= models.FloatField()
    
