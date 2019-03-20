# coding: utf-8

import random
import subprocess
import django_filters
from rest_framework import viewsets, filters
from rest_framework.response import Response

import json

from .models import Pet, Pets
from .serializer import PetSerializer, PetsSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list(self, request, *args, **kwargs):
        pet_param_dict_list = list()
        # while True:
        for i in range(5):
            score_dict = {}
            pet_param_dict = {
                "mouth_x" : random.random(),
                "mouth_y" : random.random(),
                "eye_right_x" : random.random(),
                "eye_right_y" : random.random(),
                "eye_left_x" : random.random(),
                "eye_left_y" : random.random(),
                "nose_x" : random.random(),
                "nose_y" : random.random(),
                "score" : 0,
            }
            # pythonファイルを叩く
            # subprocess.check_call(['python','error.py'])
            score = i
            pet_param_dict["score"] = score

            if (score not in score_dict):
                score_dict[score] = score
                pet_param_dict_list.append(pet_param_dict)
        
        return Response(json.dumps(pet_param_dict_list))

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

    def list(self, request, *args, **kwargs):
        pet_param_dict = {
            "mouth_x" : 0.2,
            "mouth_y" : 0.4,
            "eye_right_x" : 0.5,
            "eye_right_y" : 0.1,
            "eye_left_x" : 0.9,
            "eye_left_y" : 0.5,
            "nose_x" : 0.3,
            "nose_y" : 0.8,
         }
        # petObj = CreatePets
        # params = create_pets.create_pets()
        return Response(json.dumps(pet_param_dict))
