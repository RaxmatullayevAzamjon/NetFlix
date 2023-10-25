from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


# Create your views here.

class HelloApi(APIView):
    def get(self, request):
        d  = {
            "xabar": "Salom, Dunyo",
            "qo'shimcha": "Bu DRF'dagi 1-API'imiz bo'ladi"
        }
        return Response(d)

    def post(self,request):
        data = request.data
        d = {
            "xabar": "Post qabul qilindi",
            "Post bo'lgan ma'lumot": data
        }
        return Response(d)


class AkrtorlarApi(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar,many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            Aktyor.objects.create(
                ism = valid_data.get("ism"),
                tugilgan_sana = valid_data.get("tugilgan_sana"),
                jins = valid_data.get("jins"),
                davlat = valid_data.get("davlat")
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class AktyorAPI(APIView):
    def get(self, request, son):
        aktyor = Aktyor.objects.get(id=son)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

    def update(self, request, son):
        data = request.data
        aktyor = Aktyor.objects.filter(id=son)
        serializer = AktyorSerializer(aktyor, data=data)
        if serializer.is_valid():
            aktyor.update(
                davlat = serializer.validated_data.get("davlat")
            )
            return Response(serializer.data)
        return Response(serializer.errors)




class MenApi(APIView):
    def get(self, request):
        d = {
            "malumot": "Men Raxmatullayev Azamjon 21- yoshman TATUFF da 4 bosqich talabsiman",
            "qo'shimcha": "tel: 916922483"
        }
        return Response(d)
