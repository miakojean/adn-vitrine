from django.shortcuts import render
from rest_framework.views import APIView
from .models import (
    Article, Author, Comment, Category
)
from .serializers import (
    AuthorSerializer,
    ArticleSerializer,
    CommentSerializer,
    CategorySerializer
)

# Create your views here.
class ArticleListView(APIView):

    def get(self, request):
        articles = Article.objects.filter