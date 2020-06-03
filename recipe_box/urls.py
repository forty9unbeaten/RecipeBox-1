from django.urls import path
from recipe_box import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('author/<int:id>', views.author, name='author_detail'),
    path('recipe/<int:id>', views.recipe, name='recipe_detail'),
    path('recipe/<int:id>/edit', views.edit_recipe_view, name='edit_recipe'),
    path('recipe/<int:id>/save', views.favorite_view, name='save_recipe'),
    path('recipe/<int:id>/remove', views.remove_favorite_view, name='remove_recipe'),
    path('addauthor/', views.add_author),
    path('addrecipe/', views.add_recipe),
    path('login/', views.loginview),
    path('logout/', views.logoutview)
]
