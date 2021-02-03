from django.views import View
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.conf import settings

import json
from collections import defaultdict
from datetime import datetime


def update_news_from_json():
    if not settings.NEED_UPDATE_NEWS:
        return

    list_news = []
    with open(settings.NEWS_JSON_PATH) as f:
        for news_info in json.load(f):
            settings.NEWS_DICT_BY_ID[news_info["link"]] = news_info
            if not settings.SEARCH_PATTERN or \
                    settings.SEARCH_PATTERN in news_info["title"]:
                list_news.append(news_info)

    settings.NEWS_DICT_BY_DATE = defaultdict(list)
    list_news.sort(key=lambda x: x["created"], reverse=True)
    for news_info in list_news:
        news_date, news_time = news_info["created"].split(" ")
        settings.NEWS_DICT_BY_DATE[news_date].append(news_info)

    # drop default_dict for correct template
    settings.NEWS_DICT_BY_DATE.default_factory = None

    settings.NEED_UPDATE_NEWS = False


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news')


class MainPageView(TemplateView):
    template_name = 'news/MainPage.html'

    def get_context_data(self, **kwargs):
        if "q" in self.request.GET:
            new_search = self.request.GET.get('q')

            settings.NEED_UPDATE_NEWS = (new_search != settings.SEARCH_PATTERN)
            settings.SEARCH_PATTERN = new_search

        update_news_from_json()

        context = super().get_context_data(**kwargs)
        context['news_dict_by_date'] = settings.NEWS_DICT_BY_DATE
        return context


class NewsPageView(TemplateView):
    template_name = 'news/NewsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_news_from_json()

        news_info = settings.NEWS_DICT_BY_ID[kwargs["link"]]
        context['title'] = news_info['title']
        context['news_date'] = news_info['created']
        context['news_description'] = news_info['text']
        return context


class CreatePageView(TemplateView):
    template_name = 'news/CreateNewsPage.html'

    def post(self, request, *args, **kwargs):
        info = {"title": request.POST.get('title'),
                "text": request.POST.get('text'),
                "created": datetime.now().isoformat(sep=" ", timespec="seconds"),
                "link": max(settings.NEWS_DICT_BY_ID.keys()) + 1}

        with open(settings.NEWS_JSON_PATH, "r+") as file:
            news_data = json.load(file)
            news_data.append(info)
            file.seek(0)
            json.dump(news_data, file)

        settings.NEED_UPDATE_NEWS = True

        return redirect('/news')
