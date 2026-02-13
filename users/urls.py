from django.urls import path
from .views import health_check, register_user
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('health/', health_check),
    path('register/', register_user),
    path('login/', TokenObtainPairView.as_view()),
]