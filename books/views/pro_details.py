from books.models.product import Product
from django.views import View
from django.shortcuts import render



class ProDetails(View):
    def get(self, request):
        ids = request.GET.get('product')
        productID = int(ids)
        products = Product.get_products_by_pid(productID)
        return render(request, 'productdetails.html', {'products' : products})