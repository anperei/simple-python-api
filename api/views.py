from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_name(request, name):
    return Response({"message": f"Hello, {name}!"})

