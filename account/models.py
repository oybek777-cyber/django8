from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=40)
    describtion=models.TextField()
    locations=models.CharField(max_length=40)

