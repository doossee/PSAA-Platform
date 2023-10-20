from django.urls import path
from .views import (
    PostListAPIView, 
    PostCreateAPIView, 
    PostRetrieveUpdateDestroyAPIView, 
    PostUpdateAPIView, 
    PostInMonthAPIView,
    PostCountAPIView,
    PostPubCountAPIView,
    UserCountAPIView,
    CustomUserAPIView,
)


urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts-publish/<int:pk>', PostUpdateAPIView.as_view()),
    path('posts-in-month/', PostInMonthAPIView.as_view()),
    path('posts-count/',PostCountAPIView.as_view()),
    path('posts-pub-count/', PostPubCountAPIView.as_view()),
    path('users/me/', CustomUserAPIView.as_view()),
    path('users-count/', UserCountAPIView.as_view()),
]