from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_box.models import Recipe, Author
from recipe_box.forms import AuthorAddForm, RecipeAddForm
# Create your views here.


def index(request):
    data = Recipe.objects.all
    return render(request, 'index.html', {'data': data})


def author(request, id=0):
    author_query = Author.objects.filter(id=id).first()
    recipe_query = Recipe.objects.filter(author=id)
    return render(request, 'author.html', {
            "author": author_query,
            "recipes": recipe_query
        })


def recipe(request, id=0):
    query = Recipe.objects.filter(id=id).first()
    description = query.description.split("\n")
    instructions = query.instructions.split("\n")
    return render(request, 'recipe.html', {
            'data': query,
            "description": description,
            "instructions": instructions
        })


def add_author(request):
    html = "add_author.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = AuthorAddForm()
        return render(request, html, {"form": form})


def add_recipe(request):
    html = "add_recipe.html"

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"]
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = RecipeAddForm()
        return render(request, html, {"form": form})
