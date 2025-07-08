from django.urls import path

from hexlet_django_blog.articles.views import IndexView

app_name = "articles"

urlpatterns = [
    path("", IndexView.as_view()),
]
