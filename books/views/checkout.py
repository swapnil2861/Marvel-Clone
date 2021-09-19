from django.shortcuts import redirect, render
from django.views import View
from books.models.product import Product
from books.models.orders import Orders
from books.models.costomer import Costomer


class Checkout(View):
    def get(self, request):
        pass

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        costomer = request.session.get('costomer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, costomer, cart, products)
        
        for product in products:
            order = Orders(costomer = Costomer(id = costomer),
                           product = product,
                           price = product.price,
                           Address = address,
                           phone = phone,
                           quantity = cart.get(str(product.id)))
            # place order               
            order.save()  
            request.session['cart'] = {}
        return redirect('cart')


