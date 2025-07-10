from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from hexlet_django_blog.articles.models import Article
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Article
    template_name = "articles/index.html"
    context_object_name = "articles"
    paginate_by = 2


class ArticleView(DetailView):
    model = Article
    template_name = "articles/show.html"
    context_object_name = "article"


class ArticleFormCreateView(CreateView):
    model = Article
    fields = ["name", "body"]
    template_name = "articles/create.html"
    success_url = reverse_lazy("articles:articles_index")
