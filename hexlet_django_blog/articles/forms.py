from django import forms
from hexlet_django_blog.articles.models import Article


class ArticleForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True)
    body = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Article
        fields = ["name", "body"]
