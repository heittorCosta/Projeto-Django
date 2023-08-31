from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleAPIView)
router.register(r'planets', PlanetAPIView)
router.register(r'starships', StarshipsAPIView)


urlpatterns = router.urls
    #estamos criando a rota de acesso a API

