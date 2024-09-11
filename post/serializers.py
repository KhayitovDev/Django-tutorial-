from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at']
        
class PostSerializer(serializers.Modelserializer):
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'created_at', 'category']
    

