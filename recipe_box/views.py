from django.shortcuts import render

from recipe_box.models import Recipe, Author
# Create your views here.


def index(request):
    data = Recipe.objects.all
    return render(request, 'index.html', {'data': data})


def author(request, id=0):
    author_query = Author.objects.filter(id=id)[0]
    recipe_query = Recipe.objects.filter(author=id)
    return render(request, 'author.html', {"author": author_query, "recipes": recipe_query})


def recipe(request, id=0):
    query = Recipe.objects.filter(id=id)[0]
    # data = query.__dict__
    # print(data)
    # description = data.description.split("\n")
    # instructions = data.instructions.split("\n")
    # data.update({"description": description, "instructions": instructions})
    return render(request, 'recipe.html', {'data': query})
