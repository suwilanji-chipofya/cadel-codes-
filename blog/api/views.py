

from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from .models import Post
from rest_framework import permissions
from api.permissons import IsOwnerOrReadOnly
from api.models import Comment
from api.models import Category

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer
    
class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
