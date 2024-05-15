from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm, UserLoginForm, CategoryForm, RecipesForm
from django.forms import ModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category,Recipes

class Index(TemplateView):
    template_name = 'recipeapp/index.html'


class Success(TemplateView):
    template_name = 'recipeapp/success.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'recipeapp/user_register.html'

    # success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'recipeapp/user_login.html'
    next_page = 'index'

    # success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    """
    Выход с сайта

    """
    next_page = 'index'


class CategoryView(ListView):
    template_name = 'recipeapp/list_category.html'
    model = Category
    context = Category.objects.all()





class AddCategoryView(CreateView):
    form_class = CategoryForm
    template_name = 'recipeapp/add_category.html'
    success_url = reverse_lazy('success')


class AddRecipeView(CreateView):
    form_class = RecipesForm
    template_name = 'recipeapp/add_recipe.html'
    success_url = reverse_lazy('success')


class UpdateRecipeView(TemplateView):
    # form_class = CategoryForm
    template_name = 'recipeapp/update_recipe.html'
    # next_page = 'index'


class ListRecipeView(ListView):
    template_name = 'recipeapp/list_recipe.html'
    model = Recipes
    context = Recipes.objects.all()



