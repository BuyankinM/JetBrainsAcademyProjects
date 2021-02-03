from django.views.generic.base import TemplateView
from resume.models import Resume


class ResumesView(TemplateView):

    template_name = 'resume/resumes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()
        return context
