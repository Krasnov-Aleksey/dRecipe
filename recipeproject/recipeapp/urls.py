from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, UserRegisterView, UserLoginView, UserLogoutView, CategoryView
from .views import AddCategoryView, AddRecipeView,UpdateRecipeView, ListRecipeView
from .views import Success, add_recipe_view_m, update_recipe
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('list_category/', CategoryView.as_view(), name='list_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('add_recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('add_recipe_m/', add_recipe_view_m, name='add_recipe_m'),
    path('update_recipe/', update_recipe, name='update_recipe'),
    path('list_recipe/', ListRecipeView.as_view(), name='list_recipe'),
    path('success/', Success.as_view(), name='success'),
]
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
