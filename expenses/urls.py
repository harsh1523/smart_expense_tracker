from django.urls import path
from .views import expenses_list_create

urlpatterns = [
    path('', expenses_list_create),
]