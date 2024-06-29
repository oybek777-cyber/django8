from django.contrib import admin
from .models import Delivery,SpecialSoffer,Product
# Register your models here.
admin.site.register([Delivery,SpecialSoffer,Product])
