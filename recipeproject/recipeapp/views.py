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


class Index(TemplateView):
    # Главная страница
    template_name = 'recipeapp/index.html'


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
    context_object_name = 'category'
    context = Category.objects.all()


class AddCategoryView(CreateView):
    form_class = CategoryForm
    template_name = 'recipeapp/add_category.html'
    success_url = reverse_lazy('success')


class AddRecipeView(CreateView):
    form_class = RecipesForm
    template_name = 'recipeapp/add_recipe.html'
    success_url = reverse_lazy('success')


def sample_view(request):
    current_user = request.user


# @login_required
def add_recipe_view_m(request, pk=1):
    current_user = request.user
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, initial={
            "author_recipe": current_user})
        if form.is_valid():
            form.save()
            return render(request, 'recipeapp/success.html')
    else:
        form = RecipesForm(initial={"author_recipe": current_user})

    return render(request, 'recipeapp/add_recipe_m.html', {'form': form,
                                                           'current_user': current_user})


class UpdateRecipeView(UpdateView):
    model = Recipes
    template_name = 'recipeapp/update_recipe.html'
    context_object_name = 'recipes'
    form_class = RecipesForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи: {self.object.title}'
        return context


def update_recipe(request, pk=2):
    recipe = Recipes.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            # form.save()
            return render(request, 'recipeapp/success.html')

    else:
        form = RecipesForm(instance=recipe)
        context = {'form': form}
        return render(request, 'recipeapp/update_recipe.html', context)


class ListRecipeView(ListView):
    template_name = 'recipeapp/list_recipe.html'
    model = Recipes
    context_object_name = 'recipes'
    # context = Recipes.objects.all()
