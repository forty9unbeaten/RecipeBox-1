from django.contrib import admin

from recipe_box.models import Author, Recipe
# Register your models here.

admin.site.register(Author)
admin.site.register(Recipe)