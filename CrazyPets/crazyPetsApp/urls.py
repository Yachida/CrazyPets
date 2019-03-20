# coding: utf-8

from rest_framework import routers
from .views import PetViewSet, PetsViewSet


router = routers.DefaultRouter()
router.register(r'pet', PetViewSet)
router.register(r'pets', PetsViewSet)