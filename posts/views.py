from rest_framework.views import APIView
from rest_framework.viewsets import generics, ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import Post, PostFilter
from .serializers import (
    PostListSerializer,
    PostSerializer,
    PostUpdateSerializer,
    PostInMonthSerializer,
    PostCreateSerializer,
    CountSerializer,
    CustomUserRoleSerializer,
)
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination
import calendar
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PostFilter
    pagination_class = LimitOffsetPagination


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class PostInMonthAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request, format=None):
    
        current_year = timezone.now().year
        current_month = timezone.now().month
        num_days = calendar.monthrange(current_year, current_month)[1]
        context = []
        for day in range(1, num_days + 1):
            date = timezone.make_aware(datetime(current_year, current_month, day))
            count_by_date = Post.objects.filter(publish_date__date=date.date().isoformat()).count()
            tmp_dict = {
                "publish_date": date,
                "count": count_by_date,
            }
            context.append(tmp_dict)
        serializer = PostInMonthSerializer(context, many=True)
        return Response(serializer.data)


class PostCountAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request, format=None):
    
        count_all = Post.objects.all().count()
        context = {
            "count": count_all,
        }
        serializer = CountSerializer(context)
        return Response(serializer.data)


class PostPubCountAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request, format=None):
    
        count_is_published = Post.objects.filter(is_published=True).count()
        context = {
            "count": count_is_published,
        }
        serializer = CountSerializer(context)
        return Response(serializer.data)
    

class UserCountAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):

        count_users = User.objects.all().count()
        context = {
            "count": count_users,
        }
        serializer = CountSerializer(context)
        return Response(serializer.data)


class CustomUserAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        serializer = CustomUserRoleSerializer(request.user)
        return Response(serializer.data)


    
    