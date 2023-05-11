from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def todo(request):
    if request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)