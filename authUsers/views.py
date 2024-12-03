import email
from sre_constants import SRE_INFO_CHARSET
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import AuthUsersSerializers, LoginSerializers
from .models import AuthUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_500_INTERNAL_SERVER_ERROR
# Create your views here.



class RegisterAuthuser(GenericAPIView):

    def post(self, request):
        data = request.data
        serializer = AuthUsersSerializers(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status': HTTP_200_OK,
                'message': "User Registered successfully",
                'data': serializer.data,
            }, status=HTTP_200_OK)

class LoginAuthUser(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username'] # type: ignore
            password = serializer.validated_data['password'] # type: ignore

            try:
                user = AuthUser.objects.get(username=username)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'status': HTTP_200_OK,
                        'message': 'Login successful',
                        'tokens': {
                            'refresh': str(refresh),
                            'access': str(refresh.access_token), # type: ignore
                        }
                    }, status=HTTP_200_OK)
                else:
                    return Response({
                        'status': HTTP_401_UNAUTHORIZED,
                        'message': 'Invalid password'
                    }, status=HTTP_401_UNAUTHORIZED)
            except AuthUser.DoesNotExist:
                return Response({
                    'status': HTTP_401_UNAUTHORIZED,
                    'message': 'User does not exist'
                }, status=HTTP_401_UNAUTHORIZED)
        return Response({
            'status': HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=HTTP_400_BAD_REQUEST)