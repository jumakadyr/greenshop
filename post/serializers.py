from rest_framework import serializers

from .models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'image')


class PostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'published_at', 'image')
