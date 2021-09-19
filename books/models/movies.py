from django.db import models
import datetime

class Movies(models.Model):
    name = models.CharField(max_length=500)
    Mposter = models.ImageField(upload_to='uploads') 
    director = models.CharField(max_length=500, default='Destin Daniel Cretton')
    writer = models.CharField(max_length=500, default='David Callaham, Destin Daniel Cretton and Andrew Lanham')
    cast = models.CharField(max_length=500, default='Simu Liu, Awkwafina, Tony Leung, Michelle Yeoh, Fala Chen, Meng’er Zhang, Florian Munteanu and Ronny Chieng')
    producer = models.CharField(max_length=500, default='Kevin Feige and Jonathan Schwartz')
    Exproducer = models.CharField(max_length=500, default='Louis D\'Esposito, Victoria Alonso and Charles Newirth')
    ReleasedDate = models.DateField(default=datetime.datetime.today)
    trailer = models.FileField(upload_to='uploads', null=True)
    description = models.CharField(max_length=500)

    @staticmethod
    def get_all_products():
        return Movies.objects.all()

    # @staticmethod
    # def get_movies_by_mid(ids):
    #     return Movies.objects.filter(id__in = ids)

    @staticmethod
    def get_movies_by_pid(ids):
        return Movies.objects.filter(id = ids) 

