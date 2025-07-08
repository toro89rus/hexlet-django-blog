from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
