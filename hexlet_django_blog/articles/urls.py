from django.urls import path

from hexlet_django_blog.articles.views import (
    ArticleFormCreateView,
    ArticleFormUpdateView,
    ArticleView,
    IndexView,
)

app_name = "articles"

urlpatterns = [
    path("", IndexView.as_view(), name="articles_index"),
    path(
        "<int:pk>/update/",
        ArticleFormUpdateView.as_view(),
        name="articles_update",
    ),
    path("<int:pk>/", ArticleView.as_view(), name="article_detail"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]
