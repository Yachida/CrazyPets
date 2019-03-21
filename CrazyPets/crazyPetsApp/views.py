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
            if ("5" not in score_dict) :
                pet_param_dict = {
                    "mouth_x" : random.uniform(0.2582094576, 0.3182094576),
                    "mouth_y" : random.uniform(0.2081635821, 0.2682094576),
                    "eye_right_x" : random.uniform(0.8222340154 , 0.8722340154),
                    "eye_right_y" : random.uniform(0.1859935329 , 0.2622340154),
                    "eye_left_x" : random.uniform(0.4520359972 , 0.5122340154),
                    "eye_left_y" : random.uniform(0.4767183779 , 0.5322340154),
                    "nose_x" : random.uniform(0.4580032295 , 0.5180032295),
                    "nose_y" : random.uniform(0.8338197435 , 0.8922340154),
                    "score" : 0,
                }
                print("5通ったよ")
            # elif ("1" not in score_dict) :
            #     pet_param_dict = {
            #         "eye_left_x" : random.uniform(0.4378189111 , 0.4778189111),
            #         "eye_left_y" : random.uniform(0.5281700018 , 0.5681700018),
            #         "eye_right_x" : random.uniform(0.4892856039 , 0.5292856039),
            #         "eye_right_y" : random.uniform(0.5163825208 , 0.5763825208),
            #         "nose_x" : random.uniform(0.4857900871 , 0.5257900871),
            #         "nose_y" : random.uniform(0.5173444929 , 0.5573444929),
            #         "mouth_x" : random.uniform(0.4960467694, 0.5360467694),
            #         "mouth_y" : random.uniform(0.4408327929, 0.4808327929),
            #         "score" : 0,
            #     }
            #     print("1通ったよ")
            else :
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
                print("それ以外通ったよ")

            # pythonファイルを叩く
            try:
                res = subprocess.check_output(["python ./crazyPetsApp/scripts/predict.py " + str(pet_param_dict["mouth_x"]) + " " + str(pet_param_dict["mouth_y"]) + " " + str(pet_param_dict["eye_right_x"]) + " " + str(pet_param_dict["eye_right_y"]) + " " + str(pet_param_dict["eye_left_x"]) + " " + str(pet_param_dict["eye_left_y"]) + " " + str(pet_param_dict["nose_x"]) + " " + str(pet_param_dict["nose_y"])],shell=True)
                res = res.decode("utf-8") # resはバイナリ形式なのでデコードする
                print(res) # ここでは2を得る
                if (res < "2") :
                    score_str = "1"
                else :
                    score_str = str(Decimal(str(res)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
            except:
                print("エラー")

            pet_param_dict["score"] = score_str

            if (score_str == "0"):
                continue

            if (score_str not in score_dict):
                print(score_str)
                score_dict[score_str] = score_str
                pet_param_dict_list.append(pet_param_dict)
            
            if (len(score_dict) == 5) :
                print("データ揃った")
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
