from django.urls import path
from .views import all, detail, all2, detail2, ListAppView, DetailAppView, CreateAppView

urlpatterns = [
    path('detail/<int:android_id>', detail),
    path('all/', all),
    path('detail2/<int:ios_id>', detail2),
    path('all2/', all2),
    path('listApps/', ListAppView.as_view()),
    path('detailAppView/<int:android_id>', DetailAppView.as_view()),
    path('create/',CreateAppView.as_view()),
]