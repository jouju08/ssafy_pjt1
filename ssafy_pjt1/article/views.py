from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers.serializer import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list_create(request):
    print('tt')
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET', 'DELETE','PUT'])
def article_detail(request, article_pk):
    #단일 게시글 조회
    article=Article.objects.get(pk=article_pk)
    if request.method=='GET':
    #직렬화 진행
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        serializer=ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #외래키 데이터 입력 후 저장
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
