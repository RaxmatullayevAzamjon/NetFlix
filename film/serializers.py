from rest_framework import serializers
from .models import *

class AktyorSerializer(serializers.Serializer):
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_sana = serializers.DateField()

class KinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = "__all__"

