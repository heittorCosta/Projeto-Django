#importa a lib para serializar os dados / importa todas as models que criamos
from rest_framework import serializers
from .models import *

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
        many = True

class StarShipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starships
        fields = '__all__'
        many = True

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'                
        many = True