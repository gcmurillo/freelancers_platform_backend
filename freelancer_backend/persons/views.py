from django.shortcuts import render
from .models import Profile, ExperienceItem
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserDetailSerializer, ProfileListSerializer, ProfileDetailSerializer, ExperienceItemListSerializer, ExperienceItemDetailSerializer
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

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
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a user instance
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProfileList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Profile.objects.all()
    # serializer_class = ProfileListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileDetailSerializer
        return ProfileListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfileDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a user instance
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ExperienceItemList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = ExperienceItem.objects.all()
    # serializer_class = ExperienceItemListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExperienceItemDetailSerializer
        return ExperienceItemListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
