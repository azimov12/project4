from django.shortcuts import render, get_object_or_404
from .models import AppIOS, AppAndroid
from django.http import JsonResponse
from .serializers import AppIOsSerializer, AppAndroidSerializer

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