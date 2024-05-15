from django.urls import path
from .views import Index, UserRegisterView, UserLoginView, UserLogoutView, CategoryView
from .views import AddCategoryView, AddRecipeView,UpdateRecipeView, ListRecipeView
from .views import Success
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('list_category/', CategoryView.as_view(), name='list_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('add_recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('update_recipe/', UpdateRecipeView.as_view(), name='update_recipe'),
    path('list_recipe/', ListRecipeView.as_view(), name='list_recipe'),
    path('success/', Success.as_view(), name='success'),
]
