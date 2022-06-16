from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        # вместо '__all__', выберем нужные поля 
        # id не будем пересылать при GET запросе
        fields = ('name', 'color', 'birth_year')
