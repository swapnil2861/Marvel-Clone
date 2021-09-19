from django import views
from django.shortcuts import render
from django.views import View
from books.models.orders import Orders
from books.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        costomer = request.session.get('costomer')
        orders = Orders.get_orders_by_costomer(costomer)
        print(orders)
        return render(request, 'order.html', {'orders': orders})
