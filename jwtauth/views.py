from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
User = get_user_model()
class Registration(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "status_code": status.HTTP_201_CREATED
        }
        return Response(res, status=status.HTTP_201_CREATED)
