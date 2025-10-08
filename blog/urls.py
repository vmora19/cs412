# blog/urls.py

from django.urls import path
from .views import * 
#ShowAllView, ArticleView, RandomArticleView

urlpatterns = [
    path(r'', RandomArticleView.as_view(), name="random"),
    path(r'show_all', ShowAllView.as_view(), name="show_all"), # modified
    path('article/<int:pk>', ArticleView.as_view(), name='article'), 
    path('article/create', CreateArticleView.as_view(), name="create_article"),# new
    path('article/<int:pk>/update', UpdateArticleView.as_view(), name="update_article"),# new
    path('comment/<int:pk>/delete', DeleteCommentView.as_view(), name="delete_comment"),
]