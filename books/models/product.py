from books.models.catagory import Catagory
from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Catagory = models.ForeignKey(Catagory, default=1, on_delete=models.CASCADE)
    discription = models.CharField(max_length=400, null=True, blank=True, default="")
    image = models.ImageField(upload_to="uploads/products")
    writer = models.CharField(max_length=50, default='Clay Champman')
    artist = models.CharField(max_length=50, default='S SAKAN')
    penciler = models.CharField(max_length=50, default='Christopher Moonehyam')
    published = models.DateField(default=datetime.datetime.today)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_products_by_pid(ids):
        return Product.objects.filter(id = ids)    

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_id(catagory_id):
        if catagory_id:
            return Product.objects.filter(Catagory = catagory_id)
        else:
            return Product.get_all_products()