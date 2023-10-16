from django.apps import AppConfig

# Create a custom configuration for the 'accounts' app.
class AccountsConfig(AppConfig):
    # Define the default auto field to be used for models in this app.
    default_auto_field = "django.db.models.BigAutoField"
    
    # Specify the name of the app.
    name = "accounts"

    # Define a 'ready' method that gets executed when the app is ready.
    def ready(self):
        # Import and execute signals related to the 'accounts' app.
        import accounts.signal
