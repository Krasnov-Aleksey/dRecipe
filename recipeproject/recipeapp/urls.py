from django.urls import path
from .views import Index, UserRegisterView, UserLoginView, UserLogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
