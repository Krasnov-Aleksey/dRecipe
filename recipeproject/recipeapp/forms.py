from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta(UserCreationForm.Meta):
        fields = (UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name'))


class UserLoginForm(AuthenticationForm):
    pass
