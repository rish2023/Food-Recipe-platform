from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import math
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorator import allowed_users, unauthenticated_user
from django.urls import reverse
from django.utils.text import slugify

# Decorator to ensure that the user must be logged in to access the 'home' view.
@login_required(login_url='login')
def home(request):
    # Retrieve all recipes from the database.
    recipes = Recipes.objects.all()
    
    context = {'recipes': recipes}
    return render(request, 'accounts/dashboard.html', context)

# A view for user login.
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pname")

        # Attempt to authenticate the user.
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in and redirect to the 'home' view.
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, display an error message.
            messages.info(request, 'You have entered wrong credentials')
            
    context = {}
    return render(request, 'accounts/Login.html', context)

# A view to log the user out.
def logoutUser(request):
    logout(request)
    return redirect('login')

# A view to handle user registration.
@unauthenticated_user
def Register(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.password = make_password(user.password)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/Register.html', context)

# A view to edit user account settings.
@login_required(login_url='login')
@allowed_users(allowed_roles=['User', 'admin'])
def accountSettings(request):
    user = request.user.profile
    form = UserForm(instance=user)
    user_recipes = Recipes.objects.filter(Recipe_Owner=request.user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form, 'user_recipes': user_recipes}
    return render(request, 'accounts/account_settings.html', context)

# A view to add a new recipe.
@login_required(login_url='login')
@allowed_users(allowed_roles=['User', 'admin'])
def addRecipe(request):
    user = request.user
    auto_data = {'Recipe_Owner': user}
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = RecipeForm(initial=auto_data)
    context = {'form': form}
    return render(request, 'accounts/add_Recipe.html', context)

# A view to edit an existing recipe.
def editRecipe(request, Recipe_name):
    recipe = get_object_or_404(Recipes, Recipe_name=Recipe_name)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect("home")
    
    context = {'form': form, 'recipe': recipe}
    return render(request, 'accounts/edit_recipe.html', context)

# A view to search for recipes.
def search(request):
    query = request.GET['query']
    if len(query) > 30:
        Recipe = Recipes.objects.none()
    else:
        Recipe1 = Recipes.objects.filter(Recipe_name__icontains=query)
        Recipe2 = Recipes.objects.filter(ingredients__icontains=query)
        Recipe3 = Recipes.objects.filter(Recipe_Type__icontains=query)
        Recipe = Recipe3.union(Recipe1.union(Recipe2))

    context = {'Recipe': Recipe, 'query': query}
    return render(request, 'accounts/search.html', context)

# A view to handle user contact messages.
def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        Issue = request.POST.get('description')

        # Save the contact message to the database
        contact_message = Contact(username=username, email=email, Issue=Issue)
        contact_message.save()
        return redirect("home")

    return render(request, 'accounts/contact.html')

# A view to display a specific recipe with comments.
@login_required(login_url='login')
@allowed_users(allowed_roles=['User', 'admin'])
def filtered_recipe(request, Recipe_name):
    recipes2 = get_object_or_404(Recipes, Recipe_name=Recipe_name)
    num_comments = review.objects.filter(recipes2=recipes2).count()
    context = {'recipes2': recipes2, 'num_comments': num_comments}
    return render(request, 'accounts/filtered_recipe.html', context)

# A view to add a comment to a specific recipe.
@login_required(login_url='login')
@allowed_users(allowed_roles=['User', 'admin'])
def add_comment(request, Recipe_name):
    recipes2 = get_object_or_404(Recipes, Recipe_name=Recipe_name)

    form = CommentForm(instance=recipes2)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=recipes2)
        if form.is_valid():
            name = request.user.profile
            body = form.cleaned_data['content']
            c = review(recipes2=recipes2, username=name, content=body, timestamp=datetime.now())
            c.save()
            return redirect(reverse('filtered_recipe', args=[Recipe_name]))
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'accounts/comment_form.html', context)

# A view to delete the last comment on a specific recipe.
def delete_comment(request, Recipe_name):
    comment = review.objects.filter(recipes2=Recipe_name).last()
    recipe = comment.recipes2.Recipe_name
    comment.delete()
    return redirect(reverse('filtered_recipe', args=[recipe]))
