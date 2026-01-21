from .models import(
    Author,
    Article,
    Comment,
    Category
)
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = [
            'id', 'name', 'email'
        ]
        read_only_fields = ['id']

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'published_date',
            'updated_date', 'is_published', 'cover_image', 'category'
        ]
        read_only_fields = ['id', 'published_date', 'updated_date']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'article', 'name', 'email', 'content', 'created_date', 'is_approved'
        ]
        read_only_fields = ['id', 'created_date', 'is_approved']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'description'
        ]
        read_only_fields = ['id']


