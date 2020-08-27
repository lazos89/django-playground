from django.urls import path

# from .views import article_list_create_api_view, article_detail_api_view
from .views import (
    ArticleListCreateApiView,
    ArticleDetailApiView,
    JournalistListCreateApiView,
)

urlpatterns = [
    # path("articles", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article-detail"),
    path("articles", ArticleListCreateApiView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailApiView.as_view(), name="article-detail"),
    path(
        "journalists/", JournalistListCreateApiView.as_view(), name="journalists-list",
    ),
]
