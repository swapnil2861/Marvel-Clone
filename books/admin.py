from books.models.costomer import Costomer
from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory
from .models.costomer import Costomer
from .models.orders import Orders
from .models.movies import Movies


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','Catagory', 'id']

class AdminCatagory(admin.ModelAdmin):
    list_display = ['name']   

class AdminMovies(admin.ModelAdmin):
    list_display = ['name', 'ReleasedDate']    

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Catagory, AdminCatagory)
admin.site.register(Costomer)
admin.site.register(Orders)
admin.site.register(Movies, AdminMovies)