from django.urls import path
from .views import *

urlpatterns = [
    #estamos criando a rota de acesso a API
    path('people/', PeopleAPIView.as_view(), name='people'),
    path('people/<int:id>', PeopleAPIView.as_view(), name='peopleParameter'),
    path('planet/', PlanetAPIView.as_view(), name='planet'),
    path('planet/<int:id>', PlanetAPIView.as_view(), name='planetParameter'),
    path('starships/', StarshipsAPIView.as_view(), name='starships'),
    path('starships/<int:id>', StarshipsAPIView.as_view(), name='starshipsParameter'),
]