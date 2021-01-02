from django.shortcuts import render
from .models import Profile, ExperienceItem
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UserList(APIView):
    """
    List all users, or create a new user
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user = User.objects.create_user(
                serializer.validated_data['username'],
                serializer.validated_data['email'],
                serializer.validated_data['password']
            )
            user.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
