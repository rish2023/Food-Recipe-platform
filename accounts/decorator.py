from django.http import HttpResponse
from django.shortcuts import redirect

# Custom decorator to handle unauthenticated users.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Check if the user is already authenticated.
        if request.user.is_authenticated:
            # Redirect authenticated users to the 'home' view.
            return redirect('home')
        else:
            # Call the original view function if the user is unauthenticated.
            return view_func(request, *args, **kwargs)
    return wrapper_func

# Custom decorator to handle users with specific roles.
def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            # Check if the user belongs to any groups.
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            # Check if the user's group is in the list of allowed roles.
            if group in allowed_roles:
                # Call the original view function if the user is authorized.
                return view_func(request, *args, **kwargs)
            else:
                # Return an HTTP response with a message if the user is not authorized.
                return HttpResponse("You are not authorized")
        return wrapper_func
    return decorators
