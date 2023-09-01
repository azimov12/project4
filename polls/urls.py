from django.urls import path
from .views import all, detail, all2, detail2

urlpatterns = [
    path('detail/<int:android_id>', detail),
    path('all/', all),
    path('detail2/<int:ios_id>', detail2),
    path('all2/', all2),
]