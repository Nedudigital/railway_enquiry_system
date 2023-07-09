from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    registered_on = models.DateTimeField(default=datetime.datetime.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

    def __str__(self):
        return self.email
