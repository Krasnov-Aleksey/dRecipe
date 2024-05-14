from django.urls import path
from .views import Index, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
