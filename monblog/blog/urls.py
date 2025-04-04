from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('nouveau/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/modifier/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/supprimer/', ArticleDeleteView.as_view(), name='article_delete'),
]
