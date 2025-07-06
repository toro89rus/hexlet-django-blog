from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView


def index(request):
    return redirect(
        reverse("articles:article", kwargs={"tags": "python", "article_id": 42})
    )


def about(request):
    return render(request, "about.html")
