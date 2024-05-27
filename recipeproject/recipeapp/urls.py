from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, UserRegisterView, UserLoginView, UserLogoutView, CategoryView
from .views import AddCategoryView, ListRecipeView
from .views import Success, add_recipe_view_m, update_recipe, list_recipe, index, recipe, recipe_category
from .views import recipe_in_category, recipe_read
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('list_category/', CategoryView.as_view(), name='list_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('add_recipe/', add_recipe_view_m, name='add_recipe_m'),
    path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe'),
    # path('list_recipe/', ListRecipeView.as_view(), name='list_recipe'),
    path('list_recipe/', list_recipe, name='list_recipe'),
    path('success/', Success.as_view(), name='success'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('recipe_category/', recipe_category, name='recipe_category'),
    path('recipe_in_category/<int:category_id>/', recipe_in_category, name='recipe_in_category'),
    path('recipe_read/<int:recipe_id>/', recipe_read, name='recipe_read'),
]
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
