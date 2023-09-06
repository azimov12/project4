from django.shortcuts import render, get_object_or_404
from .models import AppIOS, AppAndroid
from django.http import JsonResponse
from .serializers import AppIOsSerializer, AppAndroidSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def detail(request, android_id): 
    apps = get_object_or_404(AppAndroid, id = android_id)
    apps_data = AppAndroidSerializer(apps)
    
    return JsonResponse(apps_data.data, safe=False)

def all(request):
    a = AppAndroid.objects.all()
    res = AppAndroidSerializer(a, many=True)
    
    return JsonResponse(res.data, safe=False)   


def detail2(request, ios_id):
    apps = get_object_or_404(AppIOS, id = ios_id)
    apps_data = AppAndroidSerializer(apps)
    
    return JsonResponse(apps_data.data, safe=False)

def all2(request):
    a = AppIOS.objects.all()
    res = AppIOsSerializer(a, many=True)
    
    return JsonResponse(res.data, safe=False)      

class ListAppView(APIView):
    def get(self, request):
        all_data = AppAndroid.objects.all()
        result = AppAndroidSerializer(all_data, many=True)
        return Response(result.data)   

class DetailAppView(APIView):
    def get(self, request, *args, **kwargs):
        app = get_object_or_404(AppAndroid, id = kwargs["android_id"])
        result = AppAndroidSerializer(app)

        return Response(result.data)

class CreateAppView(APIView):
    def post(self, request):
        user_body = request.data
        serializer = AppAndroidSerializer(data=user_body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)     
        return Response(serializer.errors)      
