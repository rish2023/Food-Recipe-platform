# Import necessary modules and classes
from cProfile import Profile
from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *  # Import models defined in your Django application
from django import forms
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create a form for user registration using UserCreationForm
class CreatUserForm(UserCreationForm):
    class Meta:
        model = User  # Specify the User model from Django's built-in auth
        fields = ['username', 'email', 'password1', 'password2',]  # Fields to include in the form

# Create a form for the User model defined in your application
class UserForm(ModelForm):
    class Meta:
        model = UserName_Profile  # Specify your custom User model
        fields = '__all__'  # Include all fields from the model
        exclude = ['user', 'password']  # Exclude the 'user' and 'password' fields from the form

# Create a form for the Recipes model defined in your application
class RecipeForm(ModelForm):
    class Meta:
        model = Recipes  # Specify your custom Recipes model
        field = "__all__"  # This is a typo; it should be "fields" to include all fields
        exclude = ['user']  # Exclude the 'user' field from the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable the 'Recipe_Owner' field so that it's read-only
        self.fields['Recipe_Owner'].widget.attrs['disabled'] = True

# Create a form for comments using a ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = review  # Specify the model for comments (replace with your actual model)
        fields = ['content',]  # Specify the fields to include in the form
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),  # Customize the 'content' field's widget
        }

# Create a form for user ratings
class RatingForm(forms.Form):
    rating = forms.DecimalField(max_digits=3, decimal_places=2)  # Define a decimal field for ratings
