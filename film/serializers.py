from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import *




class AktyorSerializer(serializers.Serializer):
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_sana = serializers.DateField()

    def validate_jins(self, qiymat):
        if qiymat == "Erkak" or qiymat == "Ayol":
            return qiymat
        raise ValidationError("Jins uchun qiymat noto'g'ri kiritildi")

    def validate_ism(self, qiymat):
        if len(qiymat) > 2:
            return qiymat
        raise ValidationError("Bunday ism bo'lishi mumkin emas")




class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = "__all__"

class KinoPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = "__all__"