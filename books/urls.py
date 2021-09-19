from django.views.generic.base import View
from books.views import order
from django.urls import path
from .views import homepage, comics, login, signup, cart, checkout, order, pro_details, movies, movie_details

urlpatterns = [
    path('home', homepage.Homepage.as_view(), name='homepage'),
    path('', comics.Comics.as_view(), name='comicpage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.Logout, name='logout'),
    path('cart',cart.Cart.as_view(), name='cart'),
    path('check-out',checkout.Checkout.as_view(), name='checkout'),
    path('Orders',order.OrderView.as_view(), name='order'),
    path('pro_details',pro_details.ProDetails.as_view()),
    path('movies',movies.MoviesPage.as_view()),
    path('movie_details',movie_details.MovieDetails.as_view())
]
