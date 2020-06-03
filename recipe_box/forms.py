from django import forms
from recipe_box.models import Author, Recipe


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']
