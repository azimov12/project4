from django.db import models
# Create your models here.

class AppIOS(models.Model):
    app_name = models.CharField(max_length=25,default='')
    app_size = models.SmallIntegerField(default = 32)
    

class AppAndroid(models.Model):
    app_name = models.CharField(max_length=25,default='')
    app_size = models.SmallIntegerField(default = 32)
       