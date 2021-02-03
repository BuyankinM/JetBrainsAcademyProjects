from django.views.generic.base import TemplateView
from django.conf import settings


MAIN_QUEUE = settings.MAIN_QUEUE


class ChangeOilView(TemplateView):
    template_name = 'get_ticket/main_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["waiting"] = len(MAIN_QUEUE["ChangeOil"]) * 2

        settings.NUM_TICKET += 1
        context["number"] = settings.NUM_TICKET

        MAIN_QUEUE["ChangeOil"].append(settings.NUM_TICKET)
        return context


class InflateTiresView(TemplateView):
    template_name = 'get_ticket/main_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["waiting"] = len(MAIN_QUEUE["ChangeOil"]) * 2 \
                             + len(MAIN_QUEUE["InflateTires"]) * 5

        settings.NUM_TICKET += 1
        context["number"] = settings.NUM_TICKET

        MAIN_QUEUE["InflateTires"].append(settings.NUM_TICKET)
        return context


class DiagnosticView(TemplateView):
    template_name = 'get_ticket/main_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["waiting"] = len(MAIN_QUEUE["ChangeOil"]) * 2 \
                             + len(MAIN_QUEUE["InflateTires"]) * 5 \
                             + len(MAIN_QUEUE["Diagnostic"]) * 30

        settings.NUM_TICKET += 1
        context["number"] = settings.NUM_TICKET

        MAIN_QUEUE["Diagnostic"].append(settings.NUM_TICKET)
        return context
