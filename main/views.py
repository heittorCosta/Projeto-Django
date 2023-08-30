from .models import *
from .serializers import *
#importa a classe de configuração da API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from 

class PeopleAPIView(APIView):
    def get(self, request, id = ''):
        if id == '':
            if 'height' in request.GET:
                peopleFound = People.objects.filter(height__gt = request.GET['height'])
                peopleSerialized = PeopleSerializer(peopleFound, many = True)
                return Response(peopleSerialized.data)
            #primeiro vamos fazer um select all do banco:
            peopleFound = People.objects.all() #select * from People
            #agora pegamos os dados em python e mandamos p/ json
            peopleSerialized = PeopleSerializer(peopleFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(peopleSerialized.data)
        else:
            try:
                peopleFound = People.objects.get(id=id)
                peopleSerialized = PeopleSerializer(peopleFound, many=False)
                return Response(peopleSerialized.data)
            except People.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND, data='People not found !!!')

    def post(self, request):
        #recebe o json que veio do cliente
        peopleJson = request.data
        peopleSerialized = PeopleSerializer(data=peopleJson)
        peopleSerialized.is_valid(raise_exception=True)
        peopleSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=peopleSerialized.data)
    
    def delete(self, request, id = ''):
        try:
            peopleFound = People.objects.get(id = id)
            peopleFound.delete()
            return Response(status=status.HTTP_200_OK, data="People successfully deleted!")
        except People.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND, data="People not Found")
        
    def put(self, request, id=id):
        peopleFound = People.objects.get(id=id)
        peopleJson = request.data
        peopleSerialized = PeopleSerializer(peopleFound, data=peopleJson)
        peopleSerialized.is_valid(raise_exception=True)
        peopleSerialized.save()
        return Response(status=status.HTTP_200_OK, data=peopleSerialized.data)
        
class PlanetAPIView(APIView):
    def get(self, request, id = ''):
        if id == '':
            #primeiro vamos fazer um select all do banco:
            planetFound = Planet.objects.all() #select * from Planet
            #agora pegamos os dados em python e mandamos p/ json
            planetSerialized = PlanetSerializer(planetFound, many = True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else:
            try:
                planetFound = Planet.objects.get(id=id) #select * from Planet
                planetSerialized = PlanetSerializer(planetFound, many = False)
                return Response(planetSerialized.data)
            except Planet.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND, data='Planet not found !!!')
class StarshipsAPIView(APIView):
    def get(self, request, id = ''):
        if id == '':
            #primeiro vamos fazer um select all do banco:
            starshipsFound = Starships.objects.all() #select * from Starships
            #agora pegamos os dados em python e mandamos p/ json
            starshipsSerialized = StarShipsSerializer(starshipsFound, many = True)
            #manda a resposta para quem chamou a API:
            return Response(starshipsSerialized.data)
        else:
            try:
                starshipsFound = Starships.objects.get(id=id) #select * from Starships
                starshipsSerialized = StarShipsSerializer(starshipsFound, many = False)
                return Response(starshipsSerialized.data)
            except Starships.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND, data='Starships not found !!!')
