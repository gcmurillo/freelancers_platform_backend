from rest_framework import serializers
from .models import Profile, ExperienceItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'country',
            'is_freelancer',
            'is_entrepreneur',
            'years_of_experience',
            'joined_at',
        ]
