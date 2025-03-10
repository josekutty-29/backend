
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm
# Assuming you have defined your User model for the existing MySQL table as discussed



def signup(request):
    if request.method == "POST":
        print("Form submitted!")  # Debug print
        print("POST data:", request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        regno = request.POST.get('regno')
        
        # Create and save the new user
        new_user = User(
            email=email,
            password=password,  # In production, use set_password() to hash the password!
            firstname=firstname,
            lastname=lastname,
            regno=regno
            # role will default to 'student' from your model
        )
        try:
            new_user.save()
        
            print("User saved successfully.")
            print("Total users now:", User.objects.count())
            # Redirect to student_register view after successful signup
            
            return redirect('student_register')
        except Exception as e:
            print("Error saving user:", e)
            messages.error(request, "Error during signup: " + str(e))
            return redirect('signup')
            
    return render(request, 'signup.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # The form field for email
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            role = user.role.lower() if hasattr(user, 'role') and user.role else ""
            
            if role == "student":
                return redirect('student_dashboard')  # URL name for student dashboard.
            elif role == "tutor":
                return redirect('tutor_dashboard')   
            elif role == "admin":
                return redirect('admin_dashboard')        # URL name for tutor page.
            else:
                
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    
    # For GET requests, render the login template.
    return render(request, 'index copy.html')

@login_required
def student_dashboard(request):
    # Prepare any context data needed for the student dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'student.html', context)

@login_required
def tutor_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'tutor.html', context)

@login_required
def admin_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'admin.html', context)    


def logout_view(request):
    logout(request)
    return redirect('login')    


""" 
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Assume the profile model has a OneToOneField linking to the user:
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_form.html', {'form': form}) """
@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Link the profile to the current user
            profile.user = request.user
            # Automatically update the registration number from the signed-up user
            profile.reg_no = request.user.regno
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Pre-populate the form with the registration number from the logged-in user
        initial_data = {
            'reg_no': request.user.regno,
            # If you want to include more defaults, add them here.
        }
        form = StudentRegistrationForm(initial=initial_data)
    return render(request, 'student_form.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # The form field for email
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            role = user.role.lower() if hasattr(user, 'role') and user.role else ""
            
            if role == "student":
                return redirect('student_dashboard')  # URL name for student dashboard.
            elif role == "tutor":
                return redirect('tutor_dashboard')   
            elif role == "admin":
                return redirect('admin_dashboard')        # URL name for tutor page.
            else:
                
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    
    # For GET requests, render the login template.
    return render(request, 'index copy.html')

@login_required
def student_dashboard(request):
    # Prepare any context data needed for the student dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'student.html', context)

@login_required
def tutor_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'tutor.html', context)

@login_required
def admin_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'admin.html', context)    


def logout_view(request):
    logout(request)
    return redirect('login')    


""" 
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Assume the profile model has a OneToOneField linking to the user:
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_form.html', {'form': form}) """
@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Link the profile to the current user
            profile.user = request.user
            # Automatically update the registration number from the signed-up user
            profile.reg_no = request.user.regno
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Pre-populate the form with the registration number from the logged-in user
        initial_data = {
            'reg_no': request.user.regno,
            # If you want to include more defaults, add them here.
        }
        form = StudentRegistrationForm(initial=initial_data)
    return render(request, 'student_form.html', {'form': form})