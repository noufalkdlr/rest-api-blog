from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["title", "content", "author", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["content", "author", "created_at"]
        read_only_fields = ["created_at"]
