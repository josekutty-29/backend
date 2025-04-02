from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        print("Form submitted!")  # Debug print
        print("POST data:", request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        regno=request.POST.get('regno')
        # Create and save the new user
        new_user = User(
            email=email,
            password=password,  # In production, hash passwords!
            firstname=firstname,
            lastname=lastname,
            regno=regno
            # role will default to 'user' from your model
        )
        try:
            new_user.save()
            print("User saved successfully.")
            print("Total users now:", User.objects.count())
        except Exception as e:
            print("Error saving user:", e)
        return redirect('signup')
    return render(request, 'signup.html')
