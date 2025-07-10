from django.views.generic import ListView, DetailView, CreateView
from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.articles.forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(ListView):
    model = Article
    template_name = "articles/index.html"
    context_object_name = "articles"
    paginate_by = 2


class ArticleView(DetailView):
    model = Article
    template_name = "articles/show.html"
    context_object_name = "article"


class ArticleFormCreateView(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/create.html"
    success_url = reverse_lazy("articles:articles_index")
    success_message = "Статья успешно добавлена"
