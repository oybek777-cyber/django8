from django.db import models

# Create your models here.
class SubCategroy(models.Model):
    name=models.CharField(max_length=40)

class Categroys(models.Model):
    name=models.CharField(max_length=40)
    categroy=models.ForeignKey(SubCategroy,on_delete=models.CASCADE)
