from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Category, Recipes


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta(UserCreationForm.Meta):
        fields = (UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name'))


class UserLoginForm(AuthenticationForm):
    pass


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name_category',)


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        widgets = {'author_recipe': forms.HiddenInput}





