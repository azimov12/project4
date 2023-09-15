from django.urls import path
from .views import AndroidAll, IOSAll, AndroidDetail, IOSDetail, CreateAndroidView, CreateIOSView, UpdateIOS, UpdateAndroid, DeleteAndroid, DeleteIOS

urlpatterns = [
    path('detail/<int:pk>', AndroidDetail.as_view()),
    path('all/', AndroidAll),
    path('detail2/<int:pk>', IOSDetail),
    path('all2/', IOSAll),
    path('create/',CreateAndroidView.as_view()),
    path('create2/',CreateIOSView.as_view()),
    path('update/<int:pk>', UpdateAndroid.as_view()),
    path('update2/<int:pk>', UpdateIOS.as_view()),
    path('delete/<int:pk>', DeleteAndroid.as_view()),
    path('delete2/<int:pk>', DeleteIOS.as_view()),
]