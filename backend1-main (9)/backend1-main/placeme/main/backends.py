from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User  # Adjust this if your user model is elsewhere

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            print("No user found with email:", username)  # Debug
            return None

        # If you have hashed the password using set_password(), use check_password:
        if (password==user.password):
            print("Password check successful for:", username)  # Debug
            return user
        else:
            print("Password check failed for:", username)  # Debug
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
