from rest_framework import serializers
from .models import CustomUser  # Import your custom user model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'phone_number', 'photo', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write-only (not shown when serialized)
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            photo=validated_data.get('photo'),
            password=validated_data['password'],
            username=validated_data['email']  # Use email as username
        )
        return user
