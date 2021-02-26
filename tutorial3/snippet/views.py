from django.shortcuts import render
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status

class GetSnippet(APIView):
    def get(self, request):
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return request(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    