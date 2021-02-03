from django.shortcuts import render
from django.views.generic.base import TemplateView
from vacancy.models import Vacancy


class VacanciesView(TemplateView):

    template_name = 'vacancy/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context
