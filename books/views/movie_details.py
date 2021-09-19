from books.models.movies import Movies
from books.models.movies import Movies
from django.views import View
from django.shortcuts import render



class MovieDetails(View):
    def get(self, request):
        ids = request.GET.get('movie')
        movieID = int(ids)
        Moviesdetails = Movies.get_movies_by_pid(movieID)
        return render(request, 'movies_details.html', {'movies' : Moviesdetails})