from rest_framework import serializers
from article.models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Article
        fields=('id', 'title', 'content',)

class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model=Comment
            fields=('id', 'comment',)
    comment_set=CommentDetailSerializer(many=True, read_only=True)
    comment_count=serializers.IntegerField(source='comment_set.count',read_only=True)
    class Meta: 
        model=Article
        fields='__all__'
        read_only_fields=('user',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Comment
        fields='__all__'
        read_only_fields=('article',)