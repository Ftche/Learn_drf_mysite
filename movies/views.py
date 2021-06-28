from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ="action")
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer

class DramaViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='drama')
    serializer_class = MovieSerializer
