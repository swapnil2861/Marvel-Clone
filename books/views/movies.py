from books.models.movies import Movies
from django.views import View
from django.shortcuts import render


class MoviesPage(View):
    def get(self, request):
        movie = Movies.get_all_products()
        return render(request, 'movies.html', {'movies' : movie})