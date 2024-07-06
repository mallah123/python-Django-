# api/serializers.py

from rest_framework import serializers
from .models import User, ContentItem, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ContentItemSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = ContentItem
        fields = ['id', 'title', 'body', 'summary', 'categories']















        # api/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ContentItem, Category

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    ...

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        return value

    class Meta:
        ...

class ContentItemSerializer(serializers.ModelSerializer):
    ...

    def validate_title(self, value):
        if len(value) > 30:
            raise serializers.ValidationError("Title must be 30 characters or less.")
        return value

    class Meta:
        ...




# api/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




# api/serializers.py

from rest_framework import serializers

class ContentSearchSerializer(serializers.Serializer):
    search_query = serializers.CharField(required=True, allow_blank=True)
