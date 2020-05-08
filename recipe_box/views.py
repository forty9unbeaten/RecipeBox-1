from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from recipe_box.models import Recipe, Author
from recipe_box.forms import AuthorAddForm, RecipeAddForm, LoginForm
# Create your views here.


def loginview(request):
    html = "loginpage.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {"form": form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


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


@login_required
def add_author(request):
    if request.user.is_staff:
        html = "add_author.html"

        if request.method == "POST":
            form = AuthorAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                    username=data["username"],
                    password=data["password"]
                )
                Author.objects.create(
                    name=data["name"],
                    bio=data["bio"],
                    user=user
                )
                return HttpResponseRedirect(reverse("homepage"))
        else:
            form = AuthorAddForm()
            return render(request, html, {"form": form})
    html = "error.html"
    return render(
        request,
        html,
        {"error": "You cannot create an author without a staff account."}
    )


@login_required
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
