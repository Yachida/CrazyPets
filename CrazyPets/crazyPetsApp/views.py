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
        path = './crazyPetsApp/input/train.csv'
        f = open(path)
        array_param = []
        array_param_split = []
        count = 1
        
        line = f.readline()
        while line:
            array_param_split = line.split(",")
            if (count == 1) :
                count = count + 1
                line = f.readline()
                continue
            if (array_param_split[8] == "5\n") :
                array_param.append(array_param_split)
            
            array_param_split = []
            line = f.readline()
        
        array_param_split = array_param[int(random.uniform(1,len(array_param)))]
        pet_param_dict_list = list()
        score_dict = {}
        # while True:
        for i in range(30):
            if ("5" not in score_dict) :
                pet_param_dict = {
                    # "mouth_x" : random.uniform(float(array_param_split[6]) - 0.01 , float(array_param_split[6]) + 0.01),
                    # "mouth_y" : random.uniform(float(array_param_split[7]) - 0.01 , float(array_param_split[7]) + 0.01),
                    # "eye_right_x" : random.uniform(float(array_param_split[2]) - 0.01 , float(array_param_split[2]) + 0.01),
                    # "eye_right_y" : random.uniform(float(array_param_split[3]) - 0.01 , float(array_param_split[3]) + 0.01),
                    # "eye_left_x" : random.uniform(float(array_param_split[0]) - 0.01 , float(array_param_split[0]) + 0.01),
                    # "eye_left_y" : random.uniform(float(array_param_split[1]) - 0.01 , float(array_param_split[1]) + 0.01),
                    # "nose_x" : random.uniform(float(array_param_split[4]) - 0.01 , float(array_param_split[4]) + 0.01),
                    # "nose_y" : random.uniform(float(array_param_split[5]) - 0.01 , float(array_param_split[5]) + 0.01),
                    # "score" : 0,
                    "mouth_x" : float(array_param_split[6]),
                    "mouth_y" : float(array_param_split[7]),
                    "eye_right_x" : float(array_param_split[2]),
                    "eye_right_y" : float(array_param_split[3]),
                    "eye_left_x" : float(array_param_split[0]),
                    "eye_left_y" : float(array_param_split[1]),
                    "nose_x" : float(array_param_split[4]),
                    "nose_y" : float(array_param_split[5]),
                    "score" : 0,
                }
                print("まだ5")
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

            # pythonファイルを叩く
            try:
                # res = subprocess.check_output(["python ./crazyPetsApp/scripts/predict.py " + str(pet_param_dict["mouth_x"]) + " " + str(pet_param_dict["mouth_y"]) + " " + str(pet_param_dict["eye_right_x"]) + " " + str(pet_param_dict["eye_right_y"]) + " " + str(pet_param_dict["eye_left_x"]) + " " + str(pet_param_dict["eye_left_y"]) + " " + str(pet_param_dict["nose_x"]) + " " + str(pet_param_dict["nose_y"])],shell=True)
                res = subprocess.check_output(["python ./crazyPetsApp/scripts/predict.py " + str(pet_param_dict["eye_left_x"]) + " " + str(pet_param_dict["eye_left_y"]) + " " + str(pet_param_dict["eye_right_x"]) + " " + str(pet_param_dict["eye_right_y"]) + " " + str(pet_param_dict["nose_x"]) + " " + str(pet_param_dict["nose_y"]) + " " + str(pet_param_dict["mouth_x"]) + " " + str(pet_param_dict["mouth_y"])],shell=True)
                print("python ./crazyPetsApp/scripts/predict.py " + str(pet_param_dict["mouth_x"]) + " " + str(pet_param_dict["mouth_y"]) + " " + str(pet_param_dict["eye_right_x"]) + " " + str(pet_param_dict["eye_right_y"]) + " " + str(pet_param_dict["eye_left_x"]) + " " + str(pet_param_dict["eye_left_y"]) + " " + str(pet_param_dict["nose_x"]) + " " + str(pet_param_dict["nose_y"]))
                res = res.decode("utf-8") # resはバイナリ形式なのでデコードする
                #print(res) # ここでは2を得る
                if (res < "2") :
                    score_str = "1"
                else :
                    score_str = str(Decimal(str(res)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
            except:
                print("エラー")

            pet_param_dict["score"] = int(score_str)

            if (score_str == "0"):
                continue

            if (score_str not in score_dict):
                print(score_str)
                score_dict[score_str] = score_str
                pet_param_dict_list.append(pet_param_dict)
            
            if (len(score_dict) == 5) :
                print("データ揃った")
                break
            print("今回のスコア:" + score_str)
            print(str(len(score_dict)) + "個揃いました")
        
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
