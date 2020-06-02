from django.urls import path
from recipe_box import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('author/<int:id>', views.author),
    path('recipe/<int:id>', views.recipe),
    path('addauthor/', views.add_author),
    path('addrecipe/', views.add_recipe),
    path('login/', views.loginview),
    path('logout/', views.logoutview)
]
