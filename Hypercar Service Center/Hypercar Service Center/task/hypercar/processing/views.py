from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import redirect


MAIN_QUEUE = settings.MAIN_QUEUE


class MainProcessingMenu(TemplateView):
    template_name = 'processing\processing_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["change_oil"] = len(MAIN_QUEUE["ChangeOil"])
        context["inflate_tires"] = len(MAIN_QUEUE["InflateTires"])
        context["diagnostic"] = len(MAIN_QUEUE["Diagnostic"])
        return context

    def post(self, request, *args, **kwargs):
        if settings.NUM_TICKET:
            settings.NUM_TICKET -= 1

            if len(MAIN_QUEUE["ChangeOil"]):
                settings.NEXT_TICKET = MAIN_QUEUE["ChangeOil"].popleft()
            elif len(MAIN_QUEUE["InflateTires"]):
                settings.NEXT_TICKET = MAIN_QUEUE["InflateTires"].popleft()
            else:
                settings.NEXT_TICKET = MAIN_QUEUE["Diagnostic"].popleft()
        else:
            settings.NEXT_TICKET = 0

        return redirect('/processing')
