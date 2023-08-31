from .models import *
from .serializers import *
#importa a classe de configuração da API
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class PeopleAPIView(ModelViewSet):
    queryset = People.objects.all() # Informa para a lib quais consultas a serem feitas
    serializer_class = PeopleSerializer # Informa o serializer
    filter_backends = [DjangoFilterBackend] #Utiliza a lib django filter
    filterset_fields = ['name', 'eyeColor', 'height', 'gender']
    permission_classes = (IsAuthenticated,)

class PlanetAPIView(ModelViewSet):
    queryset = Planet.objects.all() # Informa para a lib quais consultas a serem feitas
    serializer_class = PlanetSerializer # Informa o serializer
    filter_backends = [DjangoFilterBackend] #Utiliza a lib django filter
    filterset_fields = ['name', 'climate', 'population']

class StarshipsAPIView(ModelViewSet):
    queryset = Starships.objects.all() # Informa para a lib quais consultas a serem feitas
    serializer_class = StarShipsSerializer # Informa o serializer
    filter_backends = [DjangoFilterBackend] #Utiliza a lib django filter
    filterset_fields = ['name', 'model', 'passengers']