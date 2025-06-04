from django.urls import path
from .views import hello_name

urlpatterns = [
    path('hello/<str:name>/', hello_name),
]

