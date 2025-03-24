from django.urls import path

from post.views import PostListAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
]