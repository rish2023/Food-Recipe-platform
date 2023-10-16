from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserName_Profile
from django.contrib.auth.models import Group

# Create a profile for a user when a new user is saved.
@receiver(post_save, sender=User)    
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Get the 'User' group and assign it to the new user.
        group = Group.objects.get(name='User')
        instance.groups.add(group)

        # Create a UserName_Profile instance with user information.
        UserName_Profile.objects.create(
            user=instance,
            name=instance.username,
            Email_Id=instance.email,
            password=instance.password,
        )
        # Print a message to indicate that the profile was created.
        print("Profile created")
