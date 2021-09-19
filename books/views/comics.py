from books.models.costomer import Costomer
from books.models.product import Product
from django.shortcuts import redirect, render
from books.models.product import Product
from books.models.catagory import Catagory
from django.views import View

class Comics(View):
    def post (self, request):
       product = request.POST.get('product')
       remove = request.POST.get('remove')
       cart = request.session.get('cart')
       if cart:
          quantity = cart.get(product)
          if quantity:
             if remove:
                if quantity<=1:
                   cart.pop(product)
                else:   
                   cart[product] = quantity - 1
             else:
                cart[product] = quantity + 1
          else:
             cart[product] = 1   
       else:
          cart ={}
          cart[product] = 1
       request.session['cart'] = cart 
       return redirect('comicpage')
       

    def get (self, request):
        cart = request.session.get('cart')
        if not cart:
           request.session['cart'] = {}
        prds = None
        ctag = Catagory.get_all_catagories();
        catagoryId = request.GET.get('catagory')
        if catagoryId:
           prds = Product.get_all_products_by_id(catagoryId)
        else:
           prds = Product.get_all_products()
        return render(request, 'comics.html', {'products' :prds, 'catagories' :ctag})