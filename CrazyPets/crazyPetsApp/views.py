# coding: utf-8

import random
import subprocess
import django_filters
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.http import HttpResponse

import json

from .models import Pet, Pets
from .serializer import PetSerializer, PetsSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def list(self, request, *args, **kwargs):
        pet_param_dict_list = list()
        score_dict = {}
        # while True:
        for i in range(30):
            
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
            try:
                res = subprocess.check_output(["python3.6 ./crazyPetsApp/scripts/predict.py " + str(pet_param_dict["eye_left_x"]) + " " + str(pet_param_dict["eye_left_y"]) + " " + str(pet_param_dict["eye_right_x"]) + " " + str(pet_param_dict["eye_right_y"]) + " " + str(pet_param_dict["nose_x"]) + " " + str(pet_param_dict["nose_y"]) + " " + str(pet_param_dict["mouth_x"]) + " " + str(pet_param_dict["mouth_y"])],shell=True)
                res = res.decode("utf-8") # resはバイナリ形式なのでデコードする
                print(res) # ここでは2を得る
                score_str = str(Decimal(str(res)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
                print(score_str)
            except:
                print("エラー")
            # score = i
            pet_param_dict["score"] = score_str

            if (score_str == "0"):
                continue

            if (score_str not in score_dict):
                print(score_str)
                score_dict[score_str] = score_str
                pet_param_dict_list.append(pet_param_dict)
            
            if (len(score_dict) == 5) :
                break
        
        return HttpResponse(json.dumps(pet_param_dict_list))


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
