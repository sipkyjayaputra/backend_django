from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Article, ArticleById

urlpatterns = [
    path('article', Article.as_view()),
    path('article/<int:limit>/<int:offset>', Article.as_view()),
    path('article/<int:item_id>', ArticleById.as_view()),
]