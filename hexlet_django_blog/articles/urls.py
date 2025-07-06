from django.urls import path

from hexlet_django_blog.articles.views import ArticleView

app_name = "articles"

urlpatterns = [
    path("<str:tags>/<int:article_id>", ArticleView.as_view(), name="article"),
]
