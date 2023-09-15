from .models import AppIOS, AppAndroid
from .serializers import AppIOsSerializer, AppAndroidSerializer
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.

class AndroidDetail(generics.RetrieveAPIView):
    queryset = AppAndroid.objects.all()
    serializer_class = AppAndroidSerializer 

class AndroidAll(generics.ListAPIView):
    queryset = AppAndroid.objects.all()
    serializer_class = AppAndroidSerializer 

class IOSDetail(generics.RetrieveAPIView):
    queryset = AppIOS.objects.all()
    serializer_class = AppIOsSerializer

class IOSAll(generics.ListAPIView):
    queryset = AppIOS.objects.all()
    serializer_class = AppIOsSerializer 

class CreateAndroidView(generics.CreateAPIView):
    queryset = AppAndroid.objects.all()
    serializer_class = AppAndroidSerializer   

class CreateIOSView(generics.CreateAPIView):
    queryset = AppIOS.objects.all()
    serializer_class = AppIOsSerializer 

class DeleteAndroid(generics.DestroyAPIView):   
    queryset = AppAndroid.objects.all()
    serializer_class = AppAndroidSerializer    

class DeleteIOS(generics.DestroyAPIView):   
    queryset = AppIOS.objects.all()
    serializer_class = AppIOsSerializer    

class UpdateAndroid(generics.UpdateAPIView):   
    queryset = AppAndroid.objects.all()
    serializer_class = AppAndroidSerializer     

class UpdateIOS(generics.UpdateAPIView):   
    queryset = AppIOS.objects.all()
    serializer_class = AppIOsSerializer