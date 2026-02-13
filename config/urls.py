from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('health/', health_check),
    path('register/', register_user),
    path('login/', TokenObtainPairView.as_view()),
]