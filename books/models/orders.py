from django.db import models
from books.models.product import Product
from books.models.costomer import Costomer
import datetime

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    costomer = models.ForeignKey(Costomer, null=True,blank=True, default='', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    Address = models.CharField(max_length=500, default='', blank=True)
    phone = models.CharField(max_length=500, default='', blank=True)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    @staticmethod
    def get_orders_by_costomer(costomer_id):
        return Orders\
                .objects\
                 .filter(costomer = costomer_id)\
                     .order_by('date')
