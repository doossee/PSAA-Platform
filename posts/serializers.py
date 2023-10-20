from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username']


class PostListSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer()
    class Meta:
        model = Post
        exclude = ['content']
        depth = 1


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'is_published']


class PostSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer()
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class PostInMonthSerializer(serializers.Serializer):
    publish_date = serializers.DateTimeField()
    count = serializers.IntegerField()


class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class CustomUserRoleSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

    def get_role(self, obj):
        if obj.is_superuser:
            return 'superuser'
        elif obj.is_staff:
            return 'staff'
        else:
            return 'regular'
