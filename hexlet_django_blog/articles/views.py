from django.shortcuts import render
from django.views import View


class ArticleView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return render(
            request,
            "articles/index.html",
            context={"app_name": request.resolver_match.app_name},
        )
