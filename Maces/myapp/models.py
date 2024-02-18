from django.db import models

class User_info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    identifier = models.CharField(max_length=32, unique=True)
 