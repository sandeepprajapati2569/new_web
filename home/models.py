from django.db import models

# Create your models here.
class User_Data(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=35)
    number=models.CharField(max_length=12)
    message=models.CharField(max_length=1000)