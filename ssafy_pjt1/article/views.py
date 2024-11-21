from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.shortcuts import render
from .serializers.serializer import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework import status

@api_view(['GET'])
def article_list(request):#게시글 리스트 출력
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):#게시글 작성
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])#단일 게시글 조회
def article_detail(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise NotFound(detail="Article not found")
    if request.method=='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    
# @permission_classes([IsAuthenticated])
@api_view(['DELETE','PUT'])
def article_modify(request, article_pk):#게시글 수정 및 삭제
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise NotFound(detail="Article not found")
    if request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        serializer=ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):#댓글 달기
        try:
            article = Article.objects.get(pk=article_pk)
        except Article.DoesNotExist:
            raise NotFound(detail="Article not found")
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #외래키 데이터 입력 후 저장
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
