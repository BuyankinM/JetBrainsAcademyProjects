from django.shortcuts import render
from django.views import View


menu_urls = {
    "/get_ticket/change_oil": "Change oil",
    "/get_ticket/inflate_tires": "Inflate tires",
    "/get_ticket/diagnostic": "Get diagnostic test",
}


class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        context = {"menu_urls": menu_urls}
        return render(request, "menu/index.html", context=context)
