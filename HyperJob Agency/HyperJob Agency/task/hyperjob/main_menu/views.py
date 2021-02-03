from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django import forms
from django.shortcuts import redirect
from resume.models import Resume
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied


class MainMenuView(View):
    template_name = 'main_menu/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MySignupView(CreateView):
    template_name = 'main_menu/signup.html'
    form_class = UserCreationForm
    success_url = 'login'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'main_menu/login.html'


class HomeView(View):
    template_name = 'main_menu/home.html'

    def get(self, request, *args, **kwargs):
        context = {
            "is_authenticated": request.user.is_authenticated,
            "is_staff": request.user.is_staff,
        }
        return render(request, self.template_name, context)


class ResumeVacancyForm(forms.Form):
    description = forms.CharField(label='Description')


class NewResumeView(View):
    template_name = 'main_menu/new_resume.html'

    def get(self, request, *args, **kwargs):
        context = {"form": ResumeVacancyForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated \
                and not request.user.is_staff:
            description = request.POST.get('description')
            Resume.objects.create(description=description, author=request.user)
            return redirect('/home')
        else:
            raise PermissionDenied


class NewVacancyView(View):
    template_name = 'main_menu/new_vacancy.html'

    def get(self, request, *args, **kwargs):
        context = {"form": ResumeVacancyForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated \
                and request.user.is_staff:
            description = request.POST.get('description')
            Vacancy.objects.create(description=description, author=request.user)
            return redirect('/home')
        else:
            raise PermissionDenied
