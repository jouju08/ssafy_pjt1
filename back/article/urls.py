from django.urls import path
from . import views
app_name='article'
urlpatterns = [
    path('list/', views.article_list),
    path('<int:article_pk>/',views.article_detail ),
    path('create/',views.article_create ),
    path('<int:article_pk>/modify/',views.article_modify ),
    path('<int:article_pk>/CommentCreate/', views.comment_create),
]