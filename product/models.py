from django.db import models
from cotegroy.models import Categroys
# Create your models here.
class Delivery(models.Model):
    product=models.ImageField(upload_to='image')
    price=models.IntegerField()
    describtions=models.TextField()

    def __str__(self) -> str:
        return self.describtions

class SpecialSoffer(models.Model):
    Image=models.ImageField(upload_to='image')
    price=models.IntegerField()


class Product(models.Model):
    category=models.ForeignKey(Categroys,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='product_image')
    about_product=models.CharField(max_length=100)    


    def __str__(self) -> str:
        return self.about_product