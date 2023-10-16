from django.urls import path
from . import views

# Define URL patterns for the 'accounts' app.
urlpatterns = [
    # Map the root URL to the 'home' view.
    path('', views.home, name='home'),

    # URL for user registration.
    path('register/', views.Register, name='register'),

    # URL for user login.
    path('login/', views.loginPage, name='login'),

    # URL for user logout.
    path('logout/', views.logoutUser, name='logout'),

    # URL for account settings.
    path('account/', views.accountSettings, name='account'),

    # URL for adding a new recipe.
    path('addRecipe/', views.addRecipe, name='add'),

    # URL for searching recipes.
    path('search/', views.search, name='search'),

    # URL for contacting support.
    path('contact/', views.contact, name='contact'),

    # URL for viewing a specific recipe and comments.
    path('filtered_recipe/<str:Recipe_name>', views.filtered_recipe, name='filtered_recipe'),

    # URL for adding a comment to a specific recipe.
    path('filtered_recipe/<str:Recipe_name>/add-comment', views.add_comment, name='add-comment'),

    # URL for deleting a comment on a specific recipe.
    path('filtered_recipe/<str:Recipe_name>/delete-comment', views.delete_comment, name='delete-comment'),

    # URL for editing an existing recipe.
    path('editRecipe/<str:Recipe_name>', views.editRecipe, name='edit'),
]
