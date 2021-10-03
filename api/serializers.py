from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
from api.models import Category
from api.models import Comment
class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']

class PostSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['id','title','body','author','comments']

class UserSerializer(serializers.ModelSerializer):
    posts=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model=User
        fields=['id','username','posts','comments']
