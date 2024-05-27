from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm, UserLoginForm, CategoryForm, RecipesForm
from django.forms import ModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Recipes
from django.contrib.auth.models import User
from random import choice


# TODO delete
class Index(TemplateView):
    # Главная страница
    template_name = 'recipeapp/index.html'


def index(request):
    recipes = Recipes.objects.all()
    recipe_list = []
    recipe_rnd = []
    for item in recipes:
        recipe_list.append(item)

    for _ in range(5):
        rnd = choice(recipe_list)
        recipe_rnd.append(rnd)
        index_rnd = recipe_list.index(rnd)
        recipe_list.pop(index_rnd)
    return render(request, 'recipeapp/index.html', {'recipes': recipe_rnd})


class Success(TemplateView):
    # Страница успешного действия
    template_name = 'recipeapp/success.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'recipeapp/user_register.html'

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
    context_object_name = 'category'
    context = Category.objects.all()


class AddCategoryView(CreateView):
    form_class = CategoryForm
    template_name = 'recipeapp/add_category.html'
    success_url = reverse_lazy('success')


def add_recipe_view_m(request):
    current_user = request.user
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, initial={
            "author_recipe": current_user})
        if form.is_valid():
            form.save()
            return render(request, 'recipeapp/success.html')
    else:
        form = RecipesForm(initial={"author_recipe": current_user})

    return render(request, 'recipeapp/add_recipe_m.html',
                  {'form': form, 'current_user': current_user})


def update_recipe(request, recipe_id=2):
    recipe = Recipes.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return render(request, 'recipeapp/success.html')

    else:
        form = RecipesForm(instance=recipe)
        context = {'form': form}
        return render(request, 'recipeapp/update_recipe.html', context)


# TODO delete
class ListRecipeView(ListView):
    template_name = 'recipeapp/list_recipe.html'
    model = Recipes
    context_object_name = 'recipes'


def list_recipe(request):
    current_user = request.user
    recipes = Recipes.objects.filter(author_recipe=current_user)
    return render(request, 'recipeapp/list_recipe.html', {'recipes': recipes})


def recipe(request, recipe_id):
    recipe = Recipes.objects.get(pk=recipe_id)
    return render(request, 'recipeapp/recipe.html', {'recipe': recipe})


def recipe_category(request):
    categorys = Category.objects.all()
    return render(request, 'recipeapp/recipe_category.html', {'categorys': categorys})


def recipe_in_category(request, category_id):
    recipes = Recipes.objects.filter(recipes_category=category_id)
    return render(request, 'recipeapp/recipe_in_category.html', {'recipes': recipes})


def recipe_read(request, recipe_id=2):
    recipe = Recipes.objects.get(pk=recipe_id)
    return render(request, 'recipeapp/recipe_read.html', {'recipe': recipe})
