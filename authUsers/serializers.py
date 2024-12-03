from rest_framework import serializers
from .models import AuthUser



class AuthUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = AuthUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializers(serializers.Serializer): 
    username = serializers.CharField(
        max_length=150, 
        required=True, 
        allow_blank=False, 
        trim_whitespace=True
    )
    password = serializers.CharField(
        required=True, 
        write_only=True, 
        style={'input_type': 'password'} 
    )
    
    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Username cannot be empty or contain only whitespace.")
        return value
    
    def validate_password(self, value):
        if not value.strip():
            raise serializers.ValidationError("Password cannot be empty or contain only whitespace.")
        return value