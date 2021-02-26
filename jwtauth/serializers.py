from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validataed_data):
        username = validataed_data["username"]
        email = validataed_data["email"]
        password = validataed_data["password"]
        password2 = validataed_data["password2"]
        if(email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError({"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError({"password": "The two passwords differ."})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user