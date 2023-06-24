from django.shortcuts import render
from .serializers import MobileSerializer
from .models import Mobile
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET","POST"])
def mobile_list(request):
    if request.method == "GET":
        mobiles = Mobile.objects.all()
        serializer = MobileSerializer(mobiles, many=True) # many here because we have many records
        return JsonResponse({"data":serializer.data})
    
    if request.method == "POST":
        serializer = MobileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PUT","DELETE","GET"])      
def mobile(request,id):
    try:
        mobile = Mobile.objects.get(pk = id)
    except:
        return Response({"message":"no result found against this record"})
    if request.method == "GET":
        serializer = MobileSerializer(mobile)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MobileSerializer(mobile,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        mobile.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)




