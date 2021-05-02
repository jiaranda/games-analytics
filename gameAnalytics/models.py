from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length =200)
    password = models.CharField(max_length = 200)
    email = models.EmailField()
