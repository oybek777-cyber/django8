from django.urls import path
from .views import product,detail_product

urlpatterns=[
    path('product/',product,name='product'),
    path('detail_product/<int:id>/',detail_product,name='detail')
]