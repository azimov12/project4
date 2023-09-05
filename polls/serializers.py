from .models import AppIOS, AppAndroid
from rest_framework import serializers

class AppIOsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppIOS
        fields = ('app_name', 'app_size')

class AppAndroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppAndroid
        fields = ('app_name', 'app_size')       