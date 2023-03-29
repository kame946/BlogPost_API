from rest_framework import serializers
from .models import BlogPost

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content"]