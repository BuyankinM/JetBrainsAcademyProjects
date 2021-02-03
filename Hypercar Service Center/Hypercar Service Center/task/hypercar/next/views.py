from django.views.generic.base import TemplateView
from django.conf import settings

MAIN_QUEUE = settings.MAIN_QUEUE

class NextView(TemplateView):
    template_name = r'next\NextQ.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if settings.NEXT_TICKET:
            next_ticket = f"Next ticket #{settings.NEXT_TICKET}"
        else:
            next_ticket = f"Waiting for the next client"

        context["next_ticket"] = next_ticket
        return context
