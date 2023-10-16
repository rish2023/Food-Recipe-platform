from django.contrib import admin
from .models import *

# Register your models in the Django admin interface.

# Register the 'Recipes' model, so it can be managed through the admin panel.
admin.site.register(Recipes)

# Register the 'UserName_Profile' model, which is presumably related to user profiles.
admin.site.register(UserName_Profile)

# Register the 'review' model, possibly for managing user comments or reviews.
admin.site.register(review)

# Register the 'Contact' model for managing contact messages.
admin.site.register(Contact)
