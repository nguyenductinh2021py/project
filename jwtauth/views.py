from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import decorators, permissions, status
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])

def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
    return Response(res, status.HTTP_201_CREATED)
