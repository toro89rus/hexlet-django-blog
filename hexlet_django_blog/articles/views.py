from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hexlet_django_blog.articles.models import Article


class IndexView(ListView):
    model = Article
    template_name = "articles/index.html"
    context_object_name = "articles"
    paginate_by = 2


class ArticleView(DetailView):
    model = Article
    template_name = "articles/show.html"
    context_object_name = "article"
