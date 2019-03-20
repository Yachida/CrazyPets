# coding: utf-8

from rest_framework import serializers

from .models import Pet, Pets


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('mouth_x', 'mouth_y', 'eye_right_x', 'eye_right_y', 'eye_left_x', 'eye_left_y', 'nose_x', 'nose_y')

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('mouth_x', 'mouth_y', 'eye_right_x', 'eye_right_y', 'eye_left_x', 'eye_left_y', 'nose_x', 'nose_y')
