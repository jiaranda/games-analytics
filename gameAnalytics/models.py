from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(
        max_length=200, unique=True, null=False, blank=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=False, blank=False)
